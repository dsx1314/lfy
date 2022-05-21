import xlrd
from xlutils.copy import copy

from common.读取TXT import read_txt


def remove_demo():
    rb = xlrd.open_workbook('C:\\FTZN\\data\\carnumber.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(1,101):
        ws.write(i ,0,read_txt()[i-1])

    wb.save('C:\\FTZN\\data\\carnumber.xls')

if __name__ == '__main__':
    remove_demo()