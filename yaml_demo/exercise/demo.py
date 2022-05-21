from envyaml import EnvYAML
def read():
    env = EnvYAML('env.yml')
    print(env['information']['value'])
    print(env['information']['age'])
    print(env['information']['name'])



if __name__ == '__main__':
    read()