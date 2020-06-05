from appium import webdriver

# 定义驱动对象类
class Driver:
    driver = None
    # 定义获取对象的方法
    @classmethod
    def get_driver(self):
        #判断有无驱动对象
        if self.driver is None:
            des = {
                "platformName":"android",
                "platformVersion":"5.1",
                "deviceName":"sanxing",
                "appPackage":"com.android.settings",
                "appActivity":".Settings"
            }

            self.driver =webdriver.Remote("http://127.0.0.1:4723/wd/hub",des)
            return self.driver
        else:
            return self.driver



#    定义关闭驱动对象的方法
    @classmethod
    def quit_driver(self):
#         判断是否有驱动对象   如果有就关闭
          if self.driver:
              self.driver.quit()
              self.driver = None
