import xlrd

def read_xls_(filename):
    xls_table = xlrd.open_workbook(filename)
    sheet = xls_table.sheet_by_index(0)

    # 表名
    # table_name = sheet.name
    # print(table_name)

    # 总行数
    # rows = sheet.nrows
    # print(rows)
    #
    # # 总列数
    cols = sheet.ncols
    # print(cols)

    # # 获取行的数据
    # for i in range(rows):
    #     print(sheet.row_values(i))
    # print(sheet.row_values(0))

#     获取列的数据
    for i in range(cols):
        sheet.col_values(i)
    a = []
    a.append(sheet.col_values(0))
    a[0].pop(0)
    return a[0]


if __name__ == '__main__':
    print(read_xls_('C:\\FTZN\\data\\carnumber_copy.xls'))