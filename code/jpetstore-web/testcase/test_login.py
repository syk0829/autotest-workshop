import csv
import time
import pytest
from tools.get_driver import start_Chrome, quit_Chrome
from page.login_page import LoginPage

class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.driver = start_Chrome("http://localhost:8080/jpetstore/actions/Catalog.action")
        cls.login_page = LoginPage(cls.driver)
    @classmethod
    def teardown_class(cls):
        quit_Chrome(cls.driver)

    @pytest.mark.parametrize("user,pwd", csv.reader(open("../data/login.csv", newline='')))
    def test_login(self,user,pwd):
        self.login_page.page_sign_in(user,pwd)


