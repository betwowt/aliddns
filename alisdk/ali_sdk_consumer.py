

import json
"""
    aliyun dns api 调度类
"""


class consumer:

    data:object

    # 读取配置文件
    def __init__(self):
        with open('settings.json','r') as myfile:
            data = myfile.read()
        self.data = json.loads(data)

    # get method
    def get_data(self):
        return self.data

    # set method
    def set_data(self,data):
        self.data = data




consumer().get()