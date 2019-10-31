# 导包
import requests

# 发送查询天气的请求

response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")

# 使用json格式输出天气
print(response.json())
# 使用 text格式输出天气
print(response.text)
# 乱码调试
print("编码为:", response.encoding)

# 解决乱码方法一: 转化为二进制格式
print(response.content.decode())

# 解决方法二: 设置编码格式 后打印

response.encoding = "utf-8"
print(response.json())
