# 定义测试基类
from selenium.webdriver.support.wait import WebDriverWait

from base.driver import Driver


class PageBase:
      # 初始化
     def __init__(self):
         self.driver = Driver.get_driver()


     # 定义获取元素的方法
     def find_ele(self,loc,timeout=5,poll_frequency=1):
         # 返回定位到的元素
         return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_element(*loc))


     # 定义点击的方法
     def click_ele(self,element):
         # 调用定位元素的方法
         self.find_ele(element).click()

     # 定义获取一组元素的方法
     def find_ele_list(self,loc,timeout=5,poll_frequency=1):
        # 返回定位到的一组元素
        return WebDriverWait(self.driver,timeout,poll_frequency).until(lambda x:x.find_elements(*loc))


     # 定义输入的操作方法
     def input_ele(self,element,text):
         # 调用定位元素的方法
         self.find_ele(element).send_keys(text)