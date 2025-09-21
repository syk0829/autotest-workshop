
from page.login_page import LoginPage
from page.query_page import QueryPage
from page.add_cart_page import Add_ChartPage
from tools.get_driver import start_Chrome,quit_Chrome

class TestAddCart:
    @classmethod
    def setup_class(cls,value="fish",username="j2ee",password="j2ee"):
        cls.driver = start_Chrome("http://localhost:8080/jpetstore/actions/Catalog.action")
        cls.login_page = LoginPage(cls.driver)
        cls.query_page = QueryPage(cls.driver)
        cls.add_cart_page = Add_ChartPage(cls.driver)

        cls.login_page.page_sign_in(username, password)
        cls.query_page.page_query(value)
    @classmethod
    def teardown_class(cls):
        quit_Chrome(cls.driver)
    def test_add_cart(self):
        self.add_cart_page.page_add_cart()






