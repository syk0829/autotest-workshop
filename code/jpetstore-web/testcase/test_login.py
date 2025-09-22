import csv
import pytest
from page.login_page import LoginPage


class TestLogin:
    @pytest.mark.parametrize("username,password,expect", csv.reader(open("../data/login.csv", newline='')))
    def test_login(self, driver, config, username, password,expect):
        """统一的登录测试 - 通过数据驱动实现不同场景"""
        driver.get(config['base_url'])
        login_page = LoginPage(driver)

        login_page.page_sign_in(username, password)

        if (expect == 'success'):
            assert login_page.is_login_successful()
        else:
            assert not login_page.is_login_successful()



