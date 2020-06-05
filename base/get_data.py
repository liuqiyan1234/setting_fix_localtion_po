import os

import yaml

# 创建获取数据类
class GetData:
#     定义获取数据的方法
      def get_data(self,name):
          with open("./data"+os.sep+name) as f:
              return yaml.safe_load(f)

