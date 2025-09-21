from base.base import Base
import page

class PayPage(Base):
    # 搜索框输入
    def page_click_checkout_btn(self,):
        self.base_click(page.checkout_btn)
    # 点击搜索按钮
    def page_click_continue_btn(self):
        self.base_click(page.continue_btn)
    def page_click_confirm_btn(self):
        self.base_click(page.confirm_btn)

    # 组合
    def page_pay(self):
        self.page_click_checkout_btn()
        self.page_click_continue_btn()
        self.page_click_confirm_btn()
