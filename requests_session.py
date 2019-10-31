# 导包
import requests

# 建立session实例
session = requests.session()
# 发送Gte请求获取验证码

response_verify = session.get("http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.3476931399098593")

# 发送post请求进行登录
response_login = session.post("http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.05465273187994302",
                              data={"username": "17326067201", "password": "123456", "verify_code": "8888"})

# 打印登录结果
print(response_login.json())

# 访问我的订单页面
response_visit = session.get("http://127.0.0.1/Home/Order/order_list.html")

# 打印访问结果
print(response_visit.text)
