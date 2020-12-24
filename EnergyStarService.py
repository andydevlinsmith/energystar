from sodapy import Socrata
import csv
import logging
import os
import time

logging.basicConfig(level=logging.ERROR)

SOCRATA_TV_KEY = "vd8s-5tty"
SOCRATA_EV_KEY = "y2tt-wp6c"
SOCRATA_UPS_KEY = "ifxy-2uty"


class EnergyStarProduct:
    """Base class for energy star products."""

    def __init__(self, product_dict):
        self.product_dict = product_dict

    def validate(self):
        for field in self.get_field_names(self.required_fields):
            try:
                self.product_dict[field]
            except KeyError as e:
                extra = {'error': str(e)}
                logging.info("Missing required field: ", extra=extra)
                raise

    def load_field(self, field, type):
        raw_value = self.product_dict[field]
        value = type(raw_value)
        setattr(self, field, value)

    def load_field_list(self, field_list):
        for field_type in field_list.keys():
            for field in field_list[field_type]:
                self.load_field(field, field_type)

    def load_fields(self):
        self.load_field_list(self.required_fields)
        self.load_field_list(self.supported_fields)

    def get_field_names(self, field_list):
        names = []
        for field_type in field_list.keys():
            for field in field_list[field_type]:
                names.append(field)
        return names

    def get_all_fields(self):
        result = []
        result += self.get_field_names(self.required_fields)
        result += self.get_field_names(self.supported_fields)
        return result

    def get_fields(self):
        output = []
        for item in self.get_all_fields():
            output.append(
                {
                    'name': item,
                    'value': getattr(self, item)
                }
            )
        return output

    def get_delta_watts(self):
        raise NotImplementedError

    def add_delta_watts(self):
        self.supported_fields[float].append('delta_watts')


class TelevisionProduct(EnergyStarProduct):
    """Television object class."""

    def __init__(self, product_dict):
        super().__init__(product_dict)
        self.field_config = "tv"
        self.required_fields = {
            str: [
                "pd_id",
                "brand_name",
                "model_name"
            ],
            float: [
                'size_inches',
                'power_consumption_in_on_mode_watts',
                'maximum_on_mode_power_for_certification_watts',
                'power_consumption_in_standby_mode_watts',
                'maximum_standby_passive_mode_power_for_certification_watts'
            ]
        }
        self.supported_fields = {
            str: [
                'technology_type',
                'ethernet_supported',
                'resolution_pixels',
            ],
            float: []
        }
        self.validate()
        self.load_fields()

    def get_scaling_factor(self):
        if self.size_inches < 20:
            return .9
        elif self.size_inches < 40:
            return .85
        elif self.size_inches < 60:
            return .7
        elif self.size_inches >= 60:
            return .65
        else:
            raise ValueError('Unknown size')

    def get_delta_watts(self):
        scaling_factor = self.get_scaling_factor()
        max_standby_passive = self.maximum_standby_passive_mode_power_for_certification_watts  # noqa
        standby_consumption = self.power_consumption_in_standby_mode_watts
        max_on = self.maximum_on_mode_power_for_certification_watts
        on_consumption = self.power_consumption_in_on_mode_watts

        result = scaling_factor * (
            (max_standby_passive - standby_consumption) +
            (max_on - on_consumption)
        )
        return result


class UPSProduct(EnergyStarProduct):
    """Uninterruptible power supply object class."""

    def __init__(self, product_dict):
        super().__init__(product_dict)
        self.field_config = "ups"
        self.required_fields = {
            str: [
                "pd_id",
                "brand_name",
                "model_name"
            ],
            float: [
                'total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac',  # noqa
                'efficiency_at_25_load_min_config_lowest_dependency_ac',
                'efficiency_at_50_load_min_config_lowest_dependency_ac',
                'efficiency_at_75_load_min_config_lowest_dependency_ac',
                'efficiency_at_100_load_min_config_lowest_dependency_ac'
            ]
        }
        self.supported_fields = {
            str: [
                'active_output_power_rating_minimum_configuration_w',
                'topology_ac'
            ],
            float: [
                'height_mm',
                'width_mm',
                'depth_mm',
            ]
        }
        self.validate()
        self.load_fields()

    def get_efficiency(self, percent):
        efficiency = {
            0: {
                "time": .8,
                "efficiency": 1
            },
            25: {
                "time": .1,
                "efficiency": self.efficiency_at_25_load_min_config_lowest_dependency_ac  # noqa
            },
            50: {
                "time": .02,
                "efficiency": self.efficiency_at_50_load_min_config_lowest_dependency_ac  # noqa
            },
            75: {
                "time": .03,
                "efficiency": self.efficiency_at_75_load_min_config_lowest_dependency_ac  # noqa
            },
            100: {
                "time": .05,
                "efficiency": self.efficiency_at_100_load_min_config_lowest_dependency_ac  # noqa
            }
        }

        return efficiency.get(percent).get('time') * \
            efficiency.get(percent).get('efficiency')

    def get_delta_watts(self):
        total_input = self.total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac  # noqa
        levels = [0, 25, 50, 75, 100]
        efficiency = [self.get_efficiency(i) for i in levels]
        result = total_input * (sum(efficiency))
        return result


class EVProduct(EnergyStarProduct):
    """Electric vehicle equipment object class."""

    def __init__(self, product_dict):
        super().__init__(product_dict)
        self.field_config = "ev"
        self.required_fields = {
            str: ["pd_id", "brand_name", "model_name"],
            float: [
                'no_vehicle_mode_input_power_w',
                'no_vehicle_mode_total_allowance_w',
                'no_vehicle_mode_power_factor',
                'partial_on_mode_input_power_w',
                'partial_on_mode_total_allowance_w',
                'partial_on_mode_power_factor',
                'idle_mode_input_power_w',
                'idle_mode_total_allowance_w',
                'idle_mode_power_factor',
                'full_current_operation_mode_test_total_loss_w'
            ]
        }
        self.supported_fields = {
            str: [],
            float: [
                'max_nameplate_output_current_a',
                'input_voltage_v',
                # 'delta_watts'
            ]
        }
        self.validate()
        self.load_fields()

    def get_allowance(self, allowed_type):
        allowances = {
            "none": {
                "allowance": self.no_vehicle_mode_total_allowance_w,
                "input_power": self.no_vehicle_mode_input_power_w,
                "power_factor": self.no_vehicle_mode_power_factor
            },

            "partial": {
                "allowance": self.partial_on_mode_total_allowance_w,
                "input_power": self.partial_on_mode_input_power_w,
                "power_factor": self.partial_on_mode_power_factor
            },
            "idle": {
                "allowance": self.idle_mode_total_allowance_w,
                "input_power": self.idle_mode_input_power_w,
                "power_factor": self.idle_mode_power_factor
            }

        }

        result = (allowances.get(allowed_type).get('allowance') -
                  allowances.get(allowed_type).get('input_power')
                  ) * allowances.get(allowed_type).get('power_factor')
        return result

    def get_delta_watts(self):
        delta_watts = sum([
            self.full_current_operation_mode_test_total_loss_w,
            self.get_allowance("none"),
            self.get_allowance("partial"),
            self.get_allowance("idle")
        ])
        return delta_watts


class EnergyStarService:
    """Manage energystar client and queries."""

    def __init__(self, client=None):
        self.get_client(client)
        self.product_keys = {
            "tv": SOCRATA_TV_KEY,
            "ev": SOCRATA_EV_KEY,
            "ups": SOCRATA_UPS_KEY
        }

    def get_token(self):
        return os.environ.get('SODAPY_APPTOKEN', None)

    def get_client(self, client=None):
        if client:
            self.client = client
        else:
            token = self.get_token()
            self.client = Socrata("data.energystar.gov", token)

    def process_query(self, query):
        if query.is_search():
            return self.do_search_query(query)
        else:
            return self.do_get_query(query)

    def do_get_query(self, query):
        product = query.get_product()
        brand = query.get_brand()
        model = query.get_model()
        result = self.get(product, brand, model)
        return result

    def do_search_query(self, query):
        product = query.get_product()
        terms = query.get_terms()
        return self.search(product, terms)

    def get(self, product, brand, model):
        key = self.product_keys.get(product)
        results = self.get_data(key, brand, model)
        result_set = GetResultSet()
        result_set = self.populate_result_set(result_set, results, product)
        return result_set

    def get_data(self, key, brand, model):
        results = []
        products = self.client.get(key)
        for product in products:
            if product.get('brand_name').lower() == brand and  \
               product.get('model_name').lower() == model:
                results.append(product)
                if len(results) > 1:
                    break
        return results

    def search(self, product, terms):
        key = self.product_keys.get(product)
        results = self.search_data(key, terms)
        result_set = SearchResultSet()
        result_set = self.populate_result_set(result_set, results, product)
        return result_set

    def search_data(self, key, search_terms):
        results = []
        products = self.client.get(key)
        for product in products:
            for value in product.values():
                if search_terms in value.lower():
                    results.append(product)
        return results

    def product_factory(self, result, product):
        products = {
            'tv': TelevisionProduct,
            'ev': EVProduct,
            'ups': UPSProduct
        }
        return products.get(product)(result)

    def populate_result_set(self, result_set, results, product):
        for result in results:
            try:
                prod = self.product_factory(result, product)
                prod.delta_watts = prod.get_delta_watts()
                prod.add_delta_watts()
                result_set.add(prod)
            except KeyError as e:
                pid = result.get('pd_id')
                extra = {"pid": pid, "error": str(e)}
                logging.info("missing field error for product", extra=extra)
                continue
        return result_set


class ResultSet:
    """Base result set."""

    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def get_results(self):
        return self.products


class GetResultSet(ResultSet):
    """Output results for get queries."""

    def __init__(self):
        self.products = []

    def output_results(self):
        if not self.products:
            print("No results.")
            return

        has_multiple_results = len(self.products) > 1
        for product in self.products:

            for field in product.get_fields():
                print('{}: {}'.format(
                    field['name'],
                    getattr(product, field['name']))
                )

            if has_multiple_results:
                print('Multiple products match this brand and model.'
                      'To view more results, use the search command.')
                break


class SearchResultSet(ResultSet):
    """Output results for search queries."""

    def get_file_string(self):
        return time.strftime("%Y%m%d-%H%M%S")

    def output_results(self):
        if not self.products:
            print("No results.")
            return

        filename = 'energystar-{}.csv'.format(self.get_file_string())
        print("Saving output to {}".format(filename))
        if self.products:
            with open(filename, 'w', newline='') as csvfile:
                self.products[0].get_fields()
                fieldnames = self.products[0].get_all_fields()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for product in self.products:
                    row = {}
                    for item in product.get_fields():
                        bar = {item['name']: item['value']}
                        row.update(bar)
                    writer.writerow(row)
