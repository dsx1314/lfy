import os
from string import Template

import yaml


class ReadFileData():

    def __init__(self):
        self.BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def load_yaml(self, yaml_file_name):
        file_path = os.path.join(self.BASE_PATH, "data", yaml_file_name)
        with open(file_path, encoding='utf-8') as f:
            data=f.read()
            # data = yaml.safe_load(f)
        return data
data = ReadFileData()

def yaml_test():
    res_data = data.load_yaml("test_case.yaml")
    print("res_data", res_data)
    tempplate1 = Template(res_data)
    tempplate1_replace = tempplate1.safe_substitute({"partner": 22, "role": "23", "header": 23})
    tempplate1_json=yaml.safe_load(tempplate1_replace)
    print(tempplate1_json)
if __name__ == "__main__":
    yaml_test()

