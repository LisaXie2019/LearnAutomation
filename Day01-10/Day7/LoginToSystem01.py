"""
登入网站

Version: 1.0
Author: Lisa
Date: 2019-07-11

"""

from selenium import webdriver
from selenium.webdriver.common.keys  import Keys
import time

driver = webdriver.Ie()
driver.get('Test web link')  # Change Part
# 找到输入框 并输入指定内容
driver.find_element_by_id('txtUID').send_keys('Username')  # Change Part
driver.find_element_by_name('Storer').click()
time.sleep(1)
driver.find_element_by_id('txtPWD').send_keys('password')  # Change Part
#driver.find_element_by_id('LoginButton').click()    #Not work
driver.find_element_by_id('LoginButton').send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()
