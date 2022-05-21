from web_base.base_object import WebPage
from selenium.webdriver.common.by import By


class NewCar(WebPage):

    '''新增车场——按钮'''
    xinzeng = (By.XPATH, '//span[contains(text(),"新增车场")]')

    '''车场名称'''
    name = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[1]/div/div/input')

    '''渠道商'''
    qudaoshang = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[2]/div/div/div[1]/input')

    '''选择渠道商'''
    chose_qudaos = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[3]')

    '''工程商'''
    gongchengshang = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[3]/div/div/div[1]/input')

    '''选择工程商'''
    chose_gongchengshang = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li[2]')

    '''所属物业'''
    wuye = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[4]/div/div/label[1]/span[1]/span')

    '''车场类型'''
    leixing = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[5]/div/div/div[1]/input')

    '''选择车场类型'''
    chose_leixing = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]')

    '''车位总数'''
    chewei_math = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[6]/div/div/input')

    '''联系人'''
    lianxiren = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[7]/div/div/input')

    '''tel_phone'''
    tel_phone = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[8]/div/div/input')

    '''所在城市'''
    city = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[9]/div/div/div[1]/input')

    '''选择城市'''
    chose_city_01 = (By.XPATH, '//span[contains(text(),"北京市")]')
    chose_city_02 = (By.XPATH, '//span[contains(text(),"市辖区")]')
    chose_city_03 = (By.XPATH, '//span[contains(text(),"东城区")]')

    '''详细地址'''
    address = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[11]/div/div[1]/div[1]/input')

    '''选择地址'''
    chose_address = (By.XPATH, '//*[@id="el-autocomplete-6208-item-0"]/div/div')

    '''车场版本'''
    chechangbanben = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[12]/div/div/div[1]/input')

    '''选择车场版本'''
    chose_chechang = (By.XPATH, '//span[contains(text(),"4G上云车场")]')

    '''提交'''
    button = (By.XPATH, '//*[@id="my-master-app"]/div/section/section/main/div/div/div[2]/form/div/div/div[2]/div/div[14]/div/button[1]')

    def __init__(self,driver):
        self.driver = driver


    def new_parking(self,car_name,number,lian_name,tel_number,address_name):
        self.click_loc(self.xinzeng)
        self.input_loc(self.name,txt=car_name)