
from page.search_page import SearchPage
from page.setting_fix_localtion_page import SettingPage

# 定义初始化类对象的类
class EnterPage:
    # 定义获取设置页面的类对象的方法
    @classmethod
    def get_setting_page(cls):
        # 返回设置页面的对象
        return SettingPage()


    # 定义获取搜索页面的类对象的方法
    @classmethod
    def get_search_page(cls):
        # 返回搜索页面的对象
        return SearchPage()