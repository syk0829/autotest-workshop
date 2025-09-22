
from page.login_page import LoginPage
from page.query_page import QueryPage
from page.add_cart_page import Add_CartPage
from page.pay_page import PayPage

class TestPay:
    def test_pay(self,class_driver,config):
        class_driver.get(config['base_url'])
        login_page = LoginPage(class_driver)
        query_page = QueryPage(class_driver)
        add_cart_page = Add_CartPage(class_driver)
        pay_page = PayPage(class_driver)

        username = config.get('username', 'j2ee')
        password = config.get('password', 'j2ee')
        login_page.page_sign_in(username, password)
        query_page.page_query("fish")
        add_cart_page.page_add_cart()
        pay_page.page_pay()







