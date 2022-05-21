import random

def get_car_number():
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K',
              'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


    Chinese_demo = ['粤', '京', '鲁', '贵', '云','津','沪','渝','冀','吉','辽','黑',
               '湘','鄂','甘','晋','陕','豫','川','桂','蒙','青','藏','新','宁','琼','闽','苏','浙','赣']

    total_one = number + letter

    f = open('C:\\FTZN\\common\\dsx.txt','w')

    for i in range(100):
        # 写车牌号码的字母+数字
        u_len = random.randint(5,6)
        value_demo = "".join([random.choice(total_one) for i in range(u_len)])

        # 写车牌号码的第二个字母
        p_len = random.randint(1,1)
        value_two = "".join([random.choice(letter) for i in range(p_len)])

        # 写车牌号码的第一字
        f_len = random.randint(1,1)
        value_fisrt = "".join([random.choice(Chinese_demo) for i in range(f_len)])

        total = value_fisrt + value_two + value_demo
        f.write(f'{total}\n')
    f.close()

if __name__ == '__main__':
    get_car_number()