# 导包
import requests

# 发送post请求,进入ihrm系统
# data 就是指提交表单数据
# json 就是指提交json数据

data = {"mobile": "13800000002", "password": "123456"}
response = requests.post("http://182.92.81.159/api/sys/login", json=data)
# 打印响应数据
print(response.text)
