import time

from selenium.webdriver.common.by import By

from web_base.base_object import WebPage

class Linting(WebPage):
    '''订单管理'''
    dingdanguanli = (By.XPATH, "//span[contains(text(),'订单管理')]")

    '''临停订单'''
    lintingdingdan = (By.XPATH, "//span[contains(text(),'临停订单')]")

    '''筛选车场'''
    car_order = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/h4/div/div[1]/input')

    '''筛选车场-选择车场：2022车场'''
    car_chose = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[2]')

    '''时间范围选择'''
    time_input_click = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/div/div/div/input')

    '''输入时间：2022-01-01至今的所有报表数据'''
    time_input_ = (By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/span[1]/div/input')

    '''点击确定时间'''
    button_allright = (By.XPATH, '/html/body/div[3]/div[2]/button[2]')

    '''输入车牌号码'''
    car_input = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input')

    '''点击查询--查询所有'''
    button_all = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[1]')

    '''展开-按钮'''
    button_zhankai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[3]')

    '''停车区域'''
    car_quyu = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[3]/div/div/div[1]/input')

    '''选择区域'''
    chose_quyu = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[2]')

    '''支付场景'''
    zhifuchangjing = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[4]/div/div/div[1]/input')

    '''选择支付场景'''
    chose_changhjing = (By.XPATH, "//li[contains(text(),'出口支付')]")

    '''支付类型'''
    zhifuleixing = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[5]/div/div/div[1]/input')

    '''选择支付类型'''
    chose_leixing = (By.XPATH, '//li[contains(text(),"微信支付")]')

    '''订单状态'''
    dingdanzhaungtai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[6]/div/div/div[1]/input')

    '''选择订单状态'''
    chose_zhaungtai = (By.XPATH, '//li[contains(text(),"已退款")]')

    '''开票状态'''
    kaipiaozhuangtai = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[7]/div/div/div[1]/input')

    '''选择开票状态'''
    chose_kaipiao = (By.XPATH, '//li[contains(text(),"未开票")]')

    '''支付渠道'''
    zhifuqudao = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[8]/div/div/div[1]/input')

    '''选择支付渠道'''
    chose_qudao = (By.XPATH, '//li[contains(text(),"微信直连")]')

    '''支付分类'''
    zhifufenlei = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[9]/div/div/div[1]/input')

    '''选择支付分类'''
    chose_fenlei = (By.XPATH, '//li[contains(text(),"电子支付")]')

    '''查询按钮'''
    button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div/div[2]/div[1]/div/form/div[10]/div/button[1]')

    def __init__(self,driver):
        self.driver = driver

    def dingdan(self,input_time,input_carnumber):
        self.click_loc(self.dingdanguanli)
        self.click_loc(self.lintingdingdan)
        self.click_loc(self.car_order)
        self.click_loc(self.car_chose)
        self.click_loc(self.time_input_click)
        self.clear_loc(self.time_input_)
        self.input_loc(self.time_input_,txt=input_time)
        self.click_loc(self.button_allright)
        self.click_loc(self.button_all)
        self.click_loc(self.button_zhankai)
        self.input_loc(self.car_input, txt=input_carnumber)
        self.click_loc(self.car_quyu)
        self.click_loc(self.chose_quyu)
        self.click_loc(self.zhifuchangjing)
        self.click_loc(self.chose_changhjing)
        self.click_loc(self.zhifuleixing)
        self.click_loc(self.chose_leixing)
        self.click_loc(self.dingdanzhaungtai)
        self.click_loc(self.chose_zhaungtai)
        self.click_loc(self.kaipiaozhuangtai)
        self.click_loc(self.chose_kaipiao)
        self.click_loc(self.zhifuqudao)
        self.click_loc(self.chose_qudao)
        self.click_loc(self.zhifufenlei)
        self.click_loc(self.chose_fenlei)
        self.click_loc(self.button)
        time.sleep(2)
        self.excute_picture(file='C:\\服务商\\picture\\查询临停订单.png')