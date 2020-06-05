# 设置页面的page类
from base.base import PageBase
from page.find_element import FindElement


class SettingPage(PageBase):
    def __init__(self):
        super().__init__()

#    定义设置页面的搜索按钮
    def click_btn_search(self):
#         调用base封装的点击方法
          self.click_ele(FindElement.search_btn)

