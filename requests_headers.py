# 导包
import requests

# 设置请求头
headers = {"content-type": "application/json"}
# 发送请求
#  设置登录的数据
json_data = {"mobile": "13800000002", "password": "123456"}

response = requests.get("http://182.92.81.159/api/sys/login", json=json_data)

# 打印结果

print(response.json())