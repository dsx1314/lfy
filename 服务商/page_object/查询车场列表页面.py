import time

from selenium.webdriver.common.by import By

from web_base.base_object import WebPage


class Car(WebPage):

    '''车场管理'''
    car_guanli = (By.XPATH, "//span[contains(text(),'车场管理')]")

    '''停车列表'''
    car_liebiao = (By.XPATH, "//span[contains(text(),'停车场列表')]")

    '''车场名称'''
    car_input_name = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input')

    '''车场状态'''
    car_zhaungtai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[3]/div/div/div[1]/input')

    '''已上线'''
    car_shangxian = (By.XPATH,"//li[contains(text(),'已上线')]")

    '''未上线'''
    car_weishangxian = (By.XPATH, "//li[contains(text(),'未上线')]")

    '''查询'''
    car_chaxun = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[4]/div/button[1]')


    def __init__(self,driver):
        self.driver = driver

    def check_car(self,input_name,input_name_02):
        self.click_loc(self.car_guanli)
        self.click_loc(self.car_liebiao)
        self.input_loc(self.car_input_name,txt=input_name)
        self.click_loc(self.car_zhaungtai)
        self.click_loc(self.car_shangxian)
        self.click_loc(self.car_chaxun)
        time.sleep(2)
        self.excute_picture(file='C:\\服务商\\picture\\停车列表上线.png')
        time.sleep(2)
        self.clear_loc(self.car_input_name)
        self.input_loc(self.car_input_name,txt=input_name_02)
        self.click_loc(self.car_zhaungtai)
        self.click_loc(self.car_weishangxian)
        self.click_loc(self.car_chaxun)
        time.sleep(2)
        self.excute_picture(file='C:\\服务商\\picture\\停车列表未上线.png')












