"""
Test data.
"""

# flake8: noqa

fake_tv_data = [
    {
        'pd_id': '2328272',
        'energy_star_partner': 'NEC Display Solutions of America, Inc.',
        'brand_name': 'NEC',
        'model_name': 'E437Q',
        'model_number': 'E437Q',
        'additional_model_information': '',
        'product_type': 'Television (TV)',
        'application': 'Consumer',
        'screen_type': 'LCD',
        'size_inches': '42.51',
        'screen_area_square_inches': '772.34',
        'resolution_pixels': '3840x2160',
        'vertical_resolution': '2160p',
        'automatic_brightness_control': 'Yes',
        'is_automatic_brightness_control_enabled_by_default_when_television_is_shipped': 'No',
        'measured_on_mode_power_at_ambient_light_level_of_3_lux_watts': '48.42',
        'measured_on_mode_power_at_ambient_light_level_of_12_lux_watts': '48.47',
        'measured_on_mode_power_at_ambient_light_level_of_35_lux_watts': '69.5',
        'measured_on_mode_power_at_ambient_light_level_of_100_lux_watts': '76.15',
        'power_consumption_in_on_mode_watts': '60.64',
        'maximum_on_mode_power_for_certification_watts': '61.04',
        'power_consumption_in_standby_mode_watts': '0.5',
        'maximum_standby_passive_mode_power_for_certification_watts': '0.35',
        'ethernet_supported': 'Fast Ethernet (100 Mbit/s)',
        'wireless_technologies_supported': 'None',
        'thin_client_capability': 'No',
        'technology_type': 'Direct-lit LED',
        'features': 'Automatic Brightness Control,High Dynamic Range,User Adjustable Backlight',
        'name_s_of_preset_picture_settings_with_the_energy_saving_feature_automatic_brightness_control_enabled_by_default': '',
        'names_of_preset_picture_settings_w_o_esf_1_enabled_by_default': '',
        'names_of_other_energy_saving_features_enabled_by_default': 'N/A',
        'luminance_in_brightest_selectable_picture_setting_cd_sq_meter': '498',
        'luminance_in_default_picture_setting_cd_sq_meter': '467',
        'luminance_at_the_3_lux_illuminance_condition_cd_m_2': '154',
        'luminance_at_the_12_lux_illuminance_condition_cd_m_2': '155',
        'luminance_at_the_35_lux_illuminance_condition_cd_m_2': '359',
        'luminance_at_the_100_lux_illuminance_condition_cd_m_2': '405',
        'reported_annual_energy_consumption_kwh': '116.6',
        'date_available_on_market': '2019-03-18T00:00:00.000',
        'date_qualified': '2018-10-08T00:00:00.000',
        'markets': 'United States, Canada',
        'energy_star_model_identifier': 'ES_1021168_E437Q_10242018104805_8521147',
        'meets_most_efficient_criteria': 'No'
    }
]

fake_ups_data = [
    {
        "pd_id": "2326403",
        "energy_star_partner": "CyberPower Systems, Inc.",
        "brand_name": "CyberPower",
        "model_name": "OL3000RTN JP",
        "model_number": "OL3000RTN JP",
        "additional_model_information": "",
        "product_type": "Ac-output UPS",
        "power_conversion_mechanism": "Static",
        "minimum_configuration_tested_model_number": "OL3000RTXL2U",
        "active_output_power_rating_minimum_configuration_w": "2700",
        "apparent_output_power_rating_minimum_configuration_va": "3000",
        "maximum_configuration_tested_model_number": "",
        "apparent_output_power_rating_maximum_configuration_va": "",
        "topology_ac": "Double Conversion",
        "topology_and_product_type_combined": "ac - Double Conversion (VFI)",
        "application": "Commercial,Consumer",
        "rated_input_voltage_v_rms": "100-125",
        "rated_input_frequency_hz": "50-60",
        "rated_output_voltage_v": "100-125",
        "rated_output_frequency_hz": "50-60",
        "rack_mountable": "Yes",
        "rack_mount_height_u": "2",
        "height_mm": "88",
        "width_mm": "433",
        "depth_mm": "600",
        "normal_mode_s_input_dependency_characteristic_ac": "Voltage and Frequency Dependent,Voltage and Frequency Independent",
        "modular_ups": "No",
        "number_of_normal_modes": "Multiple-normal-mode",
        "default_normal_mode_ac": "Voltage and Frequency Independent",
        "test_input_voltage_v_rms": "120",
        "test_input_frequency_hz": "60",
        "test_output_voltage_v": "120",
        "test_output_frequency_hz": "60",
        "total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac": "46.93",
        "efficiency_at_25_load_min_config_lowest_dependency_ac": "89.8",
        "efficiency_at_50_load_min_config_lowest_dependency_ac": "91.7",
        "efficiency_at_75_load_min_config_lowest_dependency_ac": "91.6",
        "efficiency_at_100_load_min_config_lowest_dependency_ac": "91.2",
        "weighted_efficiency_calc_min_config_lowest_dependency": "91.5",
        "total_input_power_in_w_at_0_load_maximum_configuration_dc": "",
        "efficiency_at_30_load_maximum_configuration_dc": "",
        "efficiency_at_40_load_maximum_configuration_dc": "",
        "efficiency_at_50_load_maximum_configuration_dc": "",
        "efficiency_at_60_load_maximum_configuration_dc": "",
        "efficiency_at_70_load_maximum_configuration_dc": "",
        "efficiency_at_80_load_maximum_configuration_dc": "",
        "efficiency": "91.5",
        "modular_ups_module_tested_model_number": "N/A",
        "energy_storage_mechanism": "Battery",
        "energy_storage_system_technology": "Valve Regulated Lead-acid Battery",
        "energy_storage_system_configuration": "Integral",
        "energy_storage_system_removable_to_another_room": "No",
        "energy_storage_system_runtime_at_100_load_min": "4",
        "energy_storage_system_runtime_at_50_load_min": "11",
        "energy_storage_system_warranty_yr": "3",
        "energy_storage_system_information_url": "http://www.cyberpowersystems.com/",
        "battery_recycling_url": "",
        "network_connections_available": "Serial Port,USB Port,Ethernet",
        "communication_protocols": "HTTPS,HTTP,SNMP (v1, 2 or 3)",
        "communication_protocol_other": "",
        "manufacturer_take_back_program": "Yes",
        "manufacturer_take_back_program_url": "",
        "model_web_page_url": "http://www.cyberpowersystems.com",
        "test_method_guidelines": "http://www.cyberpowersystems.com/",
        "date_available_on_market": "2013-07-01T00:00:00.000",
        "date_qualified": "2018-09-19T00:00:00.000",
        "markets": "United States",
        "energy_star_model_identifier": "ES_1095904_OL3000RTN JP_09192018083920_6360648"
    },
    {
        "pd_id": "2326404",
        "energy_star_partner": "CyberPower Systems, Inc.",
        "brand_name": "CyberPower",
        "model_name": "OL3000RTXL2U",
        "model_number": "OL3000RTXL2U",
        "additional_model_information": "",
        "product_type": "Ac-output UPS",
        "power_conversion_mechanism": "Static",
        "minimum_configuration_tested_model_number": "OL3000RTXL2U",
        "active_output_power_rating_minimum_configuration_w": "2700",
        "apparent_output_power_rating_minimum_configuration_va": "3000",
        "maximum_configuration_tested_model_number": "",
        "apparent_output_power_rating_maximum_configuration_va": "",
        "topology_ac": "Double Conversion",
        "topology_and_product_type_combined": "ac - Double Conversion (VFI)",
        "application": "Commercial,Consumer",
        "rated_input_voltage_v_rms": "100-125",
        "rated_input_frequency_hz": "50-60",
        "rated_output_voltage_v": "100-125",
        "rated_output_frequency_hz": "50-60",
        "rack_mountable": "Yes",
        "rack_mount_height_u": "2",
        "height_mm": "88",
        "width_mm": "433",
        "depth_mm": "600",
        "normal_mode_s_input_dependency_characteristic_ac": "Voltage and Frequency Dependent,Voltage and Frequency Independent",
        "modular_ups": "No",
        "number_of_normal_modes": "Multiple-normal-mode",
        "default_normal_mode_ac": "Voltage and Frequency Independent",
        "test_input_voltage_v_rms": "120",
        "test_input_frequency_hz": "60",
        "test_output_voltage_v": "120",
        "test_output_frequency_hz": "60",
        "total_input_power_in_w_at_0_load_min_config_lowest_dependency_ac": "46.93",
        "efficiency_at_25_load_min_config_lowest_dependency_ac": "89.8",
        "efficiency_at_50_load_min_config_lowest_dependency_ac": "91.7",
        "efficiency_at_75_load_min_config_lowest_dependency_ac": "91.6",
        "efficiency_at_100_load_min_config_lowest_dependency_ac": "91.2",
        "weighted_efficiency_calc_min_config_lowest_dependency": "91.5",
        "total_input_power_in_w_at_0_load_maximum_configuration_dc": "",
        "efficiency_at_30_load_maximum_configuration_dc": "",
        "efficiency_at_40_load_maximum_configuration_dc": "",
        "efficiency_at_50_load_maximum_configuration_dc": "",
        "efficiency_at_60_load_maximum_configuration_dc": "",
        "efficiency_at_70_load_maximum_configuration_dc": "",
        "efficiency_at_80_load_maximum_configuration_dc": "",
        "efficiency": "91.5",
        "modular_ups_module_tested_model_number": "N/A",
        "energy_storage_mechanism": "Battery",
        "energy_storage_system_technology": "Valve Regulated Lead-acid Battery",
        "energy_storage_system_configuration": "Integral",
        "energy_storage_system_removable_to_another_room": "No",
        "energy_storage_system_runtime_at_100_load_min": "4",
        "energy_storage_system_runtime_at_50_load_min": "11",
        "energy_storage_system_warranty_yr": "3",
        "energy_storage_system_information_url": "http://www.cyberpowersystems.com/",
        "battery_recycling_url": "",
        "network_connections_available": "Serial Port,USB Port,Ethernet",
        "communication_protocols": "HTTPS,HTTP,SNMP (v1, 2 or 3)",
        "communication_protocol_other": "",
        "manufacturer_take_back_program": "Yes",
        "manufacturer_take_back_program_url": "",
        "model_web_page_url": "http://www.cyberpowersystems.com",
        "test_method_guidelines": "http://www.cyberpowersystems.com/",
        "date_available_on_market": "2013-07-01T00:00:00.000",
        "date_qualified": "2018-09-19T00:00:00.000",
        "markets": "United States",
        "energy_star_model_identifier": "ES_1095904_OL3000RTXL2U_09192018083457_6097421"
    }
]

fake_ev_data = [
    {
        "pd_id": "2304183",
        "energy_star_partner": "ChargePoint, Inc.",
        "brand_name": "ChargePoint",
        "model_name": "CT4000",
        "model_number": "CT4020-HD-GW",
        "additional_model_information": ",CT4020,; ,CT4020-GW1,; ,CT4020-HD,; ,CT4020-HD-F,; ,CT4020-HD-GW-LTE,; ,CT4021,; ,CT4021-GW1,; ,CT4021-HD,; ,CT4021-HD-GW1,; ,CT4021-HD-GW1-LEV,; ,CT4021-HD-GW1-LTE,; ,CT4023,; ,CT4023-GW1,; ,CT4023-HD,; ,CT4023-HD-GW1,; ,CT4023-HD-GW1-LET,",
        "product_type": "Level 2",
        "max_nameplate_output_current_a": "32",
        "input_voltage_v": "240",
        "number_of_outputs": "2",
        "output_cord_length_ft": "18",
        "output_cord_gauge_awg": "10",
        "screen_area_if_evse_has_high_res_display_in2": "16.88",
        "maximum_100_measured_luminance_of_the_high_res_display": "381",
        "automatic_brightness_control_abc_capable": "Yes",
        "connected_functionality_capable": "Yes",
        "connected_functionality_capabilities_summary": "All ChargePoint electric vehicle charging stations have the ability to reduce the output power delivered to the vehicle.  The output can be reduced by either a percent of the present load or set to a fixed kilowatt maximum value at the group or individual EVSE level.  ChargePoint offers an OpenADR 2.0b certified Virtual End Node interface for receiving pricing signals and demand response commands, which can be mapped to a designated group of EVSE (e.g. site, zip code, etc.) for the purpose of controlling load either directly or as a response to a pricing signal.  Pricing signals received over the network on a daily basis may be passed on to the driver or site host.  ChargePoint also offers a SOAP based web services API and a web based interface for controlling load of a group of EVSE or an individual EVSE.  In addition, EVSE can be scheduled to raise or lower output power at the individual or group level, such that the power output could be set to a different level at each 15 minute interval of the day on a recurring basis.  Near real-time load and status of the EVSE can be read from the OpenADR, SOAP API, and web interface for the purpose of feedback into a load management system, and historical reports of peak power, average power, and energy dispensed are available as clock aligned 15 minute intervals and charging session summaries.  Depending upon the type of load management program controlling the EVSE, drivers may have the option to override a power management event either through a mobile app, or by using a technique from the industry called the double pump, which is simply plugging in, unplugging, and plugging in the connector again within five seconds.  Site hosts and energy management service providers may choose to set fees or provide incentives for these actions to motivate behavior to optimize grid conditions.",
        "network_protocol_with_wake_capability": "Wi-Fi or Gigabit Ethernet,Cellular",
        "no_vehicle_mode_input_power_w": "3.68",
        "no_vehicle_mode_total_allowance_w": "10.12",
        "no_vehicle_mode_power_factor": "0.235",
        "partial_on_mode_input_power_w": "3.7",
        "partial_on_mode_total_allowance_w": "10.12",
        "partial_on_mode_power_factor": "0.47",
        "idle_mode_input_power_w": "5",
        "idle_mode_total_allowance_w": "19.72",
        "idle_mode_power_factor": "0.26",
        "full_current_operation_mode_test_total_loss_w": "16.21",
        "dual_input_level_2_no_vehicle_mode_input_power_w": "7.36",
        "dual_input_no_vehicle_mode_total_allowance_w": "9.12",
        "dual_input_level_2_no_vehicle_mode_power_factor": "0.47",
        "dual_input_level_2_partial_on_mode_input_power_w": "7.4",
        "dual_input_partial_on_mode_total_allowance_w": "9.12",
        "dual_input_level_2_partial_on_mode_power_factor": "0.47",
        "dual_input_level_2_idle_mode_input_power_w": "10",
        "dual_input_idle_mode_total_allowance_w": "18.72",
        "dual_input_level_2_idle_mode_power_factor": "0.52",
        "dual_input_level_2_full_currop_mode_test_total_lo": "1483.87",
        "dual_input_level_2_15_a_op_mode_test_total_loss": "930.215",
        "dual_input_level_2_4_a_op_mode_test_total_loss": "560.72",
        "date_available_on_market": "2017-10-01T00:00:00.000",
        "date_qualified": "2017-10-01T00:00:00.000",
        "markets": "United States, Canada",
        "energy_star_model_identifier": "ES_1132586_Cx402y-z Series_09272017211719_7039110"
    },
    {
        "pd_id": "2341067",
        "energy_star_partner": "ChargePoint, Inc.",
        "brand_name": "ChargePoint",
        "model_name": "CT4000",  # intentional dupe (was CPH50)
        "model_number": "CPH50",
        "additional_model_information": "Fleet,CPF50,; Fleet,CPF50-L18,; Fleet,CPF50-L18- PEDMNT-Dual,; Fleet,CPF50-L18-CMK6-PEDMNT-Dual,; Fleet,CPF50-L18-PEDMNT,; Fleet,CPF50-L18-PEDMNT-CMK6,; Fleet,CPF50-L18-WALLMNT-CMK6,; Fleet,CPF50-L23,; Fleet,CPF50-L23-CMK6-PEDMNT-Dual,; Fleet,CPF50-L23-PEDMNT,; Fleet,CPF50-L23-PEDMNT-CMK6,; Fleet,CPF50-L23-PEDMNT-Dual,; Fleet,CPF50-L23-WALLMNT-CMK6,; Home Flex,CPH50-NEMA14-50-L23,; Home Flex,CPH50-NEMA6-50-L23,",
        "product_type": "Level 2",
        "max_nameplate_output_current_a": "50",
        "input_voltage_v": "240",
        "number_of_outputs": "1",
        "output_cord_length_ft": "23",
        "output_cord_gauge_awg": "9",
        "automatic_brightness_control_abc_capable": "No",
        "connected_functionality_capable": "Yes",
        "connected_functionality_capabilities_summary": "All ChargePoint electric vehicle charging stations have the ability to reduce the output power delivered to the vehicle. The output can be reduced by either a percent of the present load or set to a fixed kilowatt maximum value at the group or individual EVSE level. ChargePoint offers an OpenADR 2.0b certified Virtual End Node interface for receiving pricing signals and demand response commands, which can be mapped to a designated group of EVSE (e.g. site, feeder, zip code, etc.) for the purpose of controlling load either directly or as a response to a pricing signal. Pricing signals received over the network on a daily basis may be passed on to the driver or site host. ChargePoint also offers a SOAP based web services API and a web based interface for controlling load of a group of EVSE or an individual EVSE. In addition, EVSE can be scheduled to raise or lower output power at the individual or group level, such that the power output could be set to a different level at each 15 minute interval of the day on a recurring basis. Near real-time load and status of the EVSE can be read from the OpenADR, SOAP API, and web interface for the purpose of feedback into a load management system, and historical reports of peak power, average power, and energy dispensed are available as clock aligned 15 minute intervals and charging session summaries. Depending upon the type of load management program controlling the EVSE, drivers may have the option to override a power management event either through a mobile app, or by using a technique from the industry called the double pump, which is simply plugging in, unplugging, and plugging in the connector again within five seconds. Site hosts and energy management service providers may choose to set fees or provide incentives for these actions to motivate behavior to optimize grid conditions.",
        "network_protocol_with_wake_capability": "Wi-Fi or Gigabit Ethernet",
        "no_vehicle_mode_input_power_w": "0.8",
        "no_vehicle_mode_total_allowance_w": "3.6",
        "no_vehicle_mode_power_factor": "0.22",
        "partial_on_mode_input_power_w": "1.36",
        "partial_on_mode_total_allowance_w": "3.6",
        "partial_on_mode_power_factor": "0.29",
        "idle_mode_input_power_w": "3.53",
        "idle_mode_total_allowance_w": "23.6",
        "idle_mode_power_factor": "0.4",
        "full_current_operation_mode_test_total_loss_w": "158.11",
        "_30_a_operation_mode_test_total_loss_w": "57.16",
        "_15_a_operation_mode_test_total_loss_w": "16.42",
        "_4_a_operation_mode_test_total_loss_w": "4.23",
        "date_available_on_market": "2019-06-25T00:00:00.000",
        "date_qualified": "2019-06-25T00:00:00.000",
        "markets": "United States, Canada",
        "energy_star_model_identifier": "ES_1132586_CPH50-xxx_07112019180355_8235348"
    }
]
