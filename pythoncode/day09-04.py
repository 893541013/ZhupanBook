from selenium import webdriver
from seleniumtools import find_element
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =  webdriver.Chrome(executable_path='chromedriver.exe')


driver.switch_to_alert().accept() #切换到alert中点击确定按钮
driver.switch_to_alert().dissmiss() # 切换到alert中点击取消按钮



# 1.手动登录获取已经登录得cookies
print(driver.get_cookies())

#2.请求的时候添加cookie去访问网站
driver.delete_all_cookies()
cookies = [{1,2,3,4,5}]
for cookie in cookies:
    driver.add_cookie(cookie)
driver.refresh()
