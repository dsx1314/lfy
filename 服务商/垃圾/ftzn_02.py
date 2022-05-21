from selenium import webdriver

from scripts.ftzn import cookie_demo

options = webdriver.ChromeOptions()
Cookie = cookie_demo()
options.add_argument('User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36')

driver = webdriver.Chrome(chrome_options=options)
driver.add_cookie(cookie_demo())
driver.get('http://mch.appykt.com/#/dashboard/analysis')
print('-----success-------')