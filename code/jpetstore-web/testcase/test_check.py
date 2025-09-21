
from page.login_page import LoginPage
from page.query_page import QueryPage
from page.add_cart_page import Add_ChartPage
from page.pay_page import PayPage
from page.check_page import CheckPage
from tools.get_driver import start_Chrome,quit_Chrome

class TestCheck:
    @classmethod
    def setup_class(cls):
        cls.driver = start_Chrome("http://localhost:8080/jpetstore/actions/Catalog.action")
        cls.login_page = LoginPage(cls.driver)
        cls.query_page = QueryPage(cls.driver)
        cls.add_cart_page = Add_ChartPage(cls.driver)
        cls.pay_page = PayPage(cls.driver)
        cls.check_page = CheckPage(cls.driver)
    @classmethod
    def teardown_class(cls):
        quit_Chrome(cls.driver)
    def test_check(self,value="fish",username="j2ee",password="j2ee"):
        self.login_page.page_sign_in(username, password)
        self.query_page.page_query(value)
        self.add_cart_page.page_add_cart()
        self.pay_page.page_pay()
        self.check_page.page_click_checkdetails()







