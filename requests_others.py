# 导包
import requests

# 发送请求 (put , delete, head, options)
response = requests.get("http://baidu.com")
# 获取响应数据
# response.status_code 状态码
print("响应状态码:", response.status_code)

# response.url 请求url

print("获取到URL:", response.url)
# response.encoding 查看响应头部字符编码
print("编码为:", response.encoding)
# response.headers 响应头的信息
print("响应头信息为:", response.headers)

# response.cookies cookie信息
print("获取到的cookie为:", response.cookies)
# response.text 文本形式的响应内容
print("获取文本:", response.text)
# response.content 字节形式的响应内容
# response.json() JSON形式的响应内容
