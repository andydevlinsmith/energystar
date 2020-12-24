import sys  # noqa
sys.path.insert(0, '.')  # noqa

from CommandHandler import CommandInterpreter
from EnergyStarService import EnergyStarService
from CommandHandler import Query
import unittest
from unittest.mock import MagicMock
from unittest.mock import patch
from test_data import fake_ev_data, fake_tv_data, fake_ups_data


class TestCommandHandler(unittest.TestCase):

    def setUp(self):
        self.fake_tv_data = fake_tv_data

    def test_get_command(self):
        command = 'get tv -b acme -m x-15'
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=self.fake_tv_data)
        ess_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(ess_svc)
        result = ch.parse_args(command.split())
        self.assertEqual(result.query_type, 'get')
        self.assertEqual(result.data.get('product'), 'tv')
        self.assertEqual(result.data.get('brand'), 'acme')
        self.assertEqual(result.data.get('model'), 'x-15')

    def test_search_command(self):
        command = 'search ev -t super'
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=self.fake_tv_data)
        ess_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(ess_svc)
        result = ch.parse_args(command.split())
        self.assertEqual(result.query_type, 'search')
        self.assertEqual(result.data.get('product'), 'ev')
        self.assertEqual(result.data.get('terms'), 'super')

    def test_search_command_multiple(self):
        command = 'search ev -t Super fast charger'
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=self.fake_tv_data)
        ess_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(ess_svc)
        result = ch.parse_args(command.split())
        self.assertEqual(result.query_type, 'search')
        self.assertEqual(result.data.get('product'), 'ev')
        self.assertEqual(result.data.get('terms'), 'super fast charger')


class TestGetQuery(unittest.TestCase):

    def setUp(self):
        self.fake_tv_data = fake_tv_data
        self.fake_ups_data = fake_ups_data
        self.fake_ev_data = fake_ev_data

    def run_get_test(self, fake_data, product, brand, model):
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=fake_data)
        es_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(es_svc)
        fake_args = ['get', product, '-b', brand, '-m', model]
        query = ch.parse_args(fake_args)
        result_set = es_svc.process_query(query)
        result = result_set.get_results()
        return result

    def test_tv_get(self):
        fake_data = self.fake_tv_data
        product = "tv"
        brand = "NEC"
        model = "E437Q"
        result = self.run_get_test(fake_data, product, brand, model)
        self.assertEqual(result[0].brand_name, brand)
        self.assertEqual(result[0].model_name, model)
        self.assertEqual(type(result[0].delta_watts), float)
        self.assertEqual(result[0].delta_watts, 0.174999999999999)

    def test_ups_get(self):
        fake_data = self.fake_ups_data
        product = "ups"
        brand = "CyberPower"
        model = "OL3000RTN JP"
        result = self.run_get_test(fake_data, product, brand, model)
        self.assertEqual(result[0].brand_name, brand)
        self.assertEqual(result[0].model_name, model)
        self.assertEqual(type(result[0].delta_watts), float)
        self.assertEqual(result[0].delta_watts, 888.00946)

    def test_ev_get(self):
        fake_data = self.fake_ev_data
        product = "ev"
        brand = "ChargePoint"
        model = "CT4000"
        result = self.run_get_test(fake_data, product, brand, model)
        self.assertEqual(result[0].brand_name, brand)
        self.assertEqual(result[0].model_name, model)
        self.assertEqual(type(result[0].delta_watts), float)
        self.assertEqual(result[0].delta_watts, 24.568)


class TestSearchQuery(unittest.TestCase):

    def setUp(self):
        self.fake_tv_data = fake_tv_data
        self.fake_ups_data = fake_ups_data
        self.fake_ev_data = fake_ev_data

    def run_search_test(self, fake_data, product, term):
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=fake_data)
        es_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(es_svc)
        fake_args = ['search', product, '-t', term]
        query = ch.parse_args(fake_args)
        result_set = es_svc.process_query(query)
        result = result_set.get_results()
        return result

    def test_search_single(self):
        fake_data = self.fake_ev_data
        product = "ev"
        term = "feeder"
        result = self.run_search_test(fake_data, product, term)
        self.assertEqual(result[0].pd_id, '2341067')
        self.assertEqual(type(result[0].delta_watts), float)

    def test_search_multiple(self):
        fake_data = self.fake_tv_data
        product = "tv"
        term = "fast ethernet"  # exercises casing
        result = self.run_search_test(fake_data, product, term)
        self.assertEqual(result[0].pd_id, '2328272')
        self.assertEqual(type(result[0].delta_watts), float)


class TestQueryOutput(unittest.TestCase):

    def setUp(self):
        self.fake_tv_data = fake_tv_data
        self.fake_ups_data = fake_ups_data
        self.fake_ev_data = fake_ev_data

    @patch('builtins.print')
    def test_get_multiple_results(self, mock_print):
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=self.fake_ev_data)
        es_svc = EnergyStarService(client=fake_socrata_client)
        ch = CommandInterpreter(es_svc)
        product = "ev"
        brand = "ChargePoint"
        model = "CT4000"
        fake_args = ['get', product, '-b', brand, '-m', model]
        query = ch.parse_args(fake_args)
        result_set = es_svc.process_query(query)
        result_set.get_results()
        result_set.output_results()
        mock_print.assert_called_with(
            'Multiple products match this brand and model.'
            'To view more results, use the search command.')

    @patch('builtins.print')
    def test_get_no_results(self, mock_print):
        fake_socrata_client = MagicMock()
        fake_socrata_client.get = MagicMock(return_value=self.fake_ev_data)
        product = "ev"
        brand = "ChargePoint"
        model = "Foo4000"
        data = {
            'product': product,
            'brand': brand,
            'model': model
        }
        query = Query('get', data)
        ess_svc = EnergyStarService(client=fake_socrata_client)
        result_set = ess_svc.process_query(query)
        result_set.output_results()
        mock_print.assert_called_with('No results.')


if __name__ == '__main__':
    unittest.main()
