from selenium import webdriver

driver =  webdriver.Chrome(executable_path='chromedriver.exe')


#浏览器最大化
driver.maximize_window()

#打开网址
driver.get("https://www.baidu.com")



#没有s#
# #id： 定位
# driver.find_element_by_id("kw").send_keys("python")
# #name： 定位
# driver.find_element_by_name("wd").send_keys("python")
#class：定位
# driver.find_element_by_class_name("s_ipt").send_keys("python")
#css selector: 定位 跟x.path一样 直接复制值
# driver.find_element_by_css_selector('#kw').send_keys("python")


# driver.find_element_by_id("su").click()


#点hao123超链接

driver.find_element_by_link_text("hao123").click()
driver.find_element_by_partial_link_text("hao1").click()


#通过标签定位
driver.find_elements_by_tag_name('input')

