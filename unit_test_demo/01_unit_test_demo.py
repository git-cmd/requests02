# 导包
import unittest
import requests


# 实现TPShop 登录测试类
class TPShopLoginTest(unittest.TestCase):

    # 初始化配置项
    def setUp(self):
        """开始层"""
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
        self.login_user_url = {"username": "13800138006", "password": "123456", "verify_code": "8888"}

    # 类初始化
    @classmethod
    def setUpClass(cls):
        """类初始化"""
        cls.session = requests.Session()
        pass

    # 结束时要执行的函数
    def tearDown(self):
        """结束层"""
        self.session.close()

    # 登录
    def Test01_Tpshop_Login_Success(self):
        # 获取验证码
        response = self.session.get(self.verify_url)
        # 断言获取的验证码接口返回的图片类型
        self.assertIn('image./png', response.headers.get("content-type"))
        # 发送登录请求
        response = self.session.post(self.verify_url,
                                     data=self.login_user_url)

        json_Data = response.json()  # 如果登陆失败了，那么登陆接口会返回html页面给response,此时调用response.json会报错

        # 输出登录接口的返回值
        print("登录接口:", json_Data)

        # 断言http 响应状态码为: 200 (200为预期值)
        self.assertEqual(200, response.status_code)
        # 断言status值为:1
        self.assertEqual(1, json_Data.get('status'))
        # 断言msg 的值为: 登录成功
        self.assertIn("登录成功", json_Data.get("msg"))


