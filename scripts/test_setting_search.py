# 定义测试类
import pytest

from base.driver import Driver
from base.get_data import GetData

from base.init_page import EnterPage
def get_data():
    new_list = []
    data = GetData().get_data("data.yml")
    print(data)
    # for i in data.values():
    #     new_list.append((i.get("input"),i.get("exp")))
    # return new_list
get_data()
class TestSearch:
    # 初始化类级别的开始
     def setup_class(self):
         self.driver =Driver.get_driver()



     # 初始化类级别的结束
     def teardown_class(self):
        Driver.quit_driver()



    # 定义测试方法
     @pytest.mark.parametrize("search_test,search_result",[("1","休眠"),("i","IP地址"),("m","MAC地址")])
     def test_search(self,search_test,search_result):
         # 设置页面的搜索按钮点击
         EnterPage.get_setting_page().click_btn_search()
         # 搜索页面的输入
         msg = EnterPage.get_search_page().get_message(search_test)
         assert search_result in msg

