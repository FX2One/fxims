import json
from typing import Tuple, List


class JsonLoadData:

    def load_param_json(self, json_path: str) -> List:
        with open(json_path) as f:
            return json.load(f)

    def load_values(self, json_path: str, json_index: int) -> Tuple:
        load_test_case = self.load_param_json(json_path)
        return tuple(list(load_test_case[json_index]['fields'].values()))

    def load_keys(self, json_path: str) -> str:
        load_test_case = self.load_param_json(json_path)
        load_list = list(load_test_case[0]['fields'].keys())
        list_to_str = ','.join(map(str, load_list))
        return list_to_str


class ConfigFixture:
    path = '../fixtures/'
    CATEGORY_FIXTURE = f'{path}db_category_fixture.json'
    SUPPLIER_FIXTURE = f'{path}db_supplier_fixture.json'
    PRODUCT_FIXTURE = f'{path}db_product_fixture.json'
    ORDER_FIXTURE = f'{path}db_order_fixture.json'
    TERRITORY_FIXTURE = f'{path}db_territory_fixture.json'
    EMPLOYEE_FIXTURE = f'{path}db_employee_fixture.json'
    EMPLOYEE_TERRITORIES_FIXTURE = f'{path}db_employee_territories_fixture.json'
    SHIPPER_FIXTURE = f'{path}db_shipper_fixture.json'
    CUSTOMER_FIXTURE = f'{path}db_customer_fixture.json'
    ORDER_DETAILS_FIXTURE = f'{path}db_order_details_fixture.json'
    REGION_FIXTURE = f'{path}db_region_fixture.json'
