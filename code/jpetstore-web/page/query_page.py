from base.base import Base
import page

class QueryPage(Base):
    # 搜索框输入
    def page_input_query(self,value):
        self.base_input(page.query_box,value)
    # 点击搜索按钮
    def page_click_query(self):
        self.base_click(page.query_btn)

    # 组合
    def page_query(self,value):
        self.page_input_query(value)
        self.page_click_query()

