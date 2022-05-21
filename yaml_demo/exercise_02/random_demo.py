import random
#
# def random_str():
#     str = ""
#     for i in range(6):
#         ch = chr(random.randrange(ord('0'), ord('9') + 1))
#         str += ch
#
#     print(str)
#
# if __name__ == '__main__':
#     random_str()




def rand_str():
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    u_len = random.randint(4,4)
    value_demo = "".join([random.choice(number) for i in range(u_len)])
    return value_demo


if __name__ == '__main__':
    print(rand_str())