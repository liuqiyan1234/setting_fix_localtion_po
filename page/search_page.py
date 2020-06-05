from base.base import PageBase

# 搜索页面的page类
from page.find_element import FindElement


class SearchPage(PageBase):
    # 定义搜索框输入内容和返回断言的方法
    def get_message(self,text):
        # 调用base类的输入方法
        self.input_ele(FindElement.search_input,text)
        # 调用base类的获取一组元素的方法
        result = self.find_ele_list(FindElement.search_result_list)
        # 列表推导式返回一组文本
        return [i.text for i in result]
