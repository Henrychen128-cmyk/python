# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome()

# 開啟 Google 首頁
browser.get('https://www.google.com.tw')

inputElement = browser.find_element_by_name("q")

inputElement.send_keys("test")

inputElement.submit()
element = browser.find_element_by_name("LC201b")
for i in element:
  print(i)
