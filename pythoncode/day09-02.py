from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =  webdriver.Chrome(executable_path='chromedriver.exe')


#浏览器最大化
driver.maximize_window()

#打开网址
driver.get("https://www.taobao.com/")


driver.find_element_by_id('q').send_keys("包包")
driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()
driver.find_element_by_id('fm-login-id').send_keys("13438093291")
driver.find_element_by_id('fm-login-password').send_keys("zp1457381758")
# driver.find_element_by_id()
# try:
#   slider = driver.find_element_by_xpath("//span[contains(@class, 'btn_slide')]")
#   if slider.is_displayed():
#     ActionChains(driver).click_and_hold(on_element=slider).perform()
#     ActionChains(driver).move_by_offset(xoffset=300, yoffset=0).perform()
#     ActionChains(driver).pause(0.5).release().perform()
# except:
#   pass
# driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
price = driver.find_element_by_xpath('//*[@id="mainsrp-itemlist"]/div/div/div[1]/div[1]/div[2]/div[1]/div[1]/strong')
assert price.text =="299.00"


driver.find_element_by_id('J_Itemlist_Pic_651109922209')
assert len(goods) !=0