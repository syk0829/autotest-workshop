from base.base import Base
import page

class CheckPage(Base):
    # 搜索框输入
    def page_click_checkdetails(self,):
        self.base_click(page.detail_btn2)