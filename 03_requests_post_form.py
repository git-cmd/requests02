# 导包
import requests

# 发送获取验证码请求
response_verify = requests.get("http://127.0.0.1/index.php?m=Home&c=User&a=verify&r=0.3476931399098593")

# 登录
response_login = requests.post("http://127.0.0.1/index.php?m=Home&c=User&a=do_login&t=0.05465273187994302",
                               data={"username": "17326067201", "password": "123456", "verify_code": "8888"})
# 打印登录结果
print(response_login.json())
