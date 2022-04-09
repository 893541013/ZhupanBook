#selenium01 1h1min处 代码

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def find_element(driver,locator,timeout = 60):
    """
        方法名:显示等待，动态查找元素
        参数：
            driver：浏览器得句柄/把柄
            locator：元素定得方式和值


            timeout：超时时间，默认为60    
    
    
    """


    return WebDriverWait(driver,timeout).until(lambda s: s.find_element(*locator))

