import os
import shutil


def remove(filepath):
    '''如果文件夹不存在则创建，'''
    if not os.path.exists(filepath):
        os.mkdir(filepath)
    else:
        '''若文件夹存在，清空文件的方法'''
        shutil.rmtree(filepath)
        os.mkdir(filepath)

if __name__ == '__main__':
    remove('C:\\服务商\\picture')