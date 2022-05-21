def read_txt():
    f = open('C:\\FTZN\\common\\dsx.txt' ,'r')

    a = list(f)
    print(a)
    return a

if __name__ == '__main__':
    print(read_txt())
