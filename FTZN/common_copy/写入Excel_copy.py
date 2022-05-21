import xlrd
from xlutils.copy import copy

from common.读取TXT import read_txt
from common_copy.读取TXT_copy import read_txt_dsx


def remove_demo_():
    rb = xlrd.open_workbook('C:\\FTZN\\data\\carnumber_copy.xls')
    wb = copy(rb)
    ws = wb.get_sheet(0)
    for i in range(1,101):
        ws.write(i ,0,read_txt_dsx()[i-1])

    wb.save('C:\\FTZN\\data\\carnumber_copy.xls')

if __name__ == '__main__':
    remove_demo_()