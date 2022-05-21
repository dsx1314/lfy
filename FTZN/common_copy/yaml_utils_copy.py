import yaml


# 写入
def write_yaml(file,data):
    with open(file,encoding='utf-8',mode='a') as f:
        yaml.dump(data,stream=f,allow_unicode=True)


# 清理
def clear_yaml(file):
    with open(file,encoding='utf-8',mode='w') as f:
        f.truncate()

# 读取
def read_yaml(file,key):
    with open(file, encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

# 读取所有
def read_all_yaml(file):
    with open(file, encoding='utf-8') as f:
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value

if __name__ == '__main__':
    print(read_yaml('C:\\FTZN\\data\\token_demo.yaml',"accessToken"))