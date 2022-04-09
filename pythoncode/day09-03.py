#切换作用域
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver =  webdriver.Chrome(executable_path='chromedriver.exe')

# 把作用域切换到网页

e =  driver.find_element_by_id() #e 就是iframe元素
driver.switch_to_frame(e)


#切换进小网页中才能定位


#切完小网页，不能再定位大网页中的元素，必须要切换回来，代码如下：
driver.switch_to_default_content()    # 把作用域切换到大网页


# 获取网页得句柄
e = driver.window_handles()
print(e)

