import json


class JsonLoadData:

    def load_param_json(self,json_path):
        with open(json_path) as f:
            return json.load(f)


    def load_values(self,json_path,json_index):
        load_test_case = self.load_param_json(json_path)
        return tuple(list(load_test_case[json_index]['fields'].values()))


    def load_keys(self,json_path):
        load_test_case = self.load_param_json(json_path)
        load_list = list(load_test_case[0]['fields'].keys())
        list_to_str = ','.join(map(str,load_list))
        return list_to_str


class ConfigFixture:

    SUPPLIER_FIXTURE = '../fixtures/db_supplier_fixture.json'




