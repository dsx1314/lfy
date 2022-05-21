from string import Template

import yaml

from exercise_02.random_demo import rand_str


def yaml_template(file,value):
    with open(file) as f:
        re = Template(f.read()).safe_substitute(value)
        print(re)
        return yaml.safe_load(re)

if __name__ == '__main__':
    print(yaml_template('C:\\yaml_demo\\data\\demo.yaml',{'user':rand_str()}))