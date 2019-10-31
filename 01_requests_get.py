# 导包
import requests

# 发送get请求
response = requests.get("http://www.baidu.com/s?wd='巴啦啦小魔仙'")

# 打印响应数据到控制台

print(response.text)
