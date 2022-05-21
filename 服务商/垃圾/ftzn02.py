#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time  : 2020/12/20 11:10
# @Author : huni
# @File  : 使用cookies登录csdn.py
# @Software: PyCharm
import time

from selenium import webdriver
import json
def browser_initial():
  browser = webdriver.Chrome()
  browser.maximize_window()
  options = webdriver.ChromeOptions()
  options.add_argument('User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36')
  browser.get(
    'http://mch.appykt.com/#/dashboard/zoo')
  return browser

def log_csdn(browser):
  with open('dsx.txt', 'r', encoding='utf8') as f:
    listCookies = json.loads(f.read())
    print(listCookies)

  # 往browser里添加cookies
  for cookie in listCookies:
    cookie_dict = {
      'domain': 'mch.appykt.com',
      'name': cookie.get('name'),
      'value': cookie.get('value'),
      "expires": '',
      'path': '/',
      'httpOnly': False,
      'HostOnly': False,
      'secure': False
    }
    browser.add_cookie(cookie_dict)

  time.sleep(5)
  browser.refresh() # 刷新网页,cookies才成功

if __name__ == "__main__":
  browser = browser_initial()
  log_csdn(browser)