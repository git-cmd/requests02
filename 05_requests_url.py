# 导包
import requests

# 发送待请求参数的URL
# 通过URL中的请求参数来发送请求(如:http://www.baidu.com/s?wd=xxx)
# response = requests.get("http://www.baidu.com/s?wd=哪吒")
# response_z = requests.get("http://www.baidu.com/s", params="wd=小猪佩奇")
response_x = requests.get("http://www.baidu.com/s", params={"wd": "海绵宝宝"})
# 查看响应结果
# print(response.text)
# print(response_z.text)
print(response_x.text)
