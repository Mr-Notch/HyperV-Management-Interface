# -- coding: utf-8 --
import json

with open('../config/config.json','r',encoding='utf8')as fp:
    config_data = json.load(fp)
    print('这是文件中的json数据：',config_data)
    print('这是读取到文件数据的数据类型：', type(config_data))