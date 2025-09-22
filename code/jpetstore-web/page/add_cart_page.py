from base.base import Base
import page

class Add_CartPage(Base):
    # 搜索框输入
    def page_click_details(self,):
        self.base_click(page.detail_btn)
    # 点击搜索按钮
    def page_click_add_cart(self):
        self.base_click(page.add_cart_btn)

    # 组合
    def page_add_cart(self):
        self.page_click_details()
        self.page_click_add_cart()
