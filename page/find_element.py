# 创建元素对象类
from selenium.webdriver.common.by import By


class FindElement:

    # 设置页面的元素
    # 搜索按钮
    search_btn = (By.ID,"com.android.settings:id/search")



    # 搜索页面的元素
#     搜索输入框
    search_input = (By.ID,"android:id/search_src_text")
#   搜索的结果
    search_result_list = (By.ID,"com.android.settings:id/title")
