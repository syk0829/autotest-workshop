import page
from base.base import Base

class LoginPage(Base):
    # 点击登录
    def page_click_login(self):
        self.base_click(page.login_btn)
    # 输入账号
    def page_input_username(self,username):
        self.base_input(page.username,username)
    # 输入密码
    def page_input_password(self,password):
        self.base_input(page.password,password)
    # 点击登录按钮
    def page_click_login_submit(self):
        self.base_click(page.login_submit)

    # 组合
    def page_sign_in(self,username,password):
        self.page_click_login()
        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_submit()