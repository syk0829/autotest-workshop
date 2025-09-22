import csv
import pytest
from page.login_page import LoginPage
from page.query_page import QueryPage
class TestQuery:
    @pytest.mark.parametrize("value", csv.reader(open("../data/query.csv", newline='')))
    def test_query(self,class_driver,config,value):
        class_driver.get(config['base_url'])
        login_page = LoginPage(class_driver)
        query_page = QueryPage(class_driver)

        username = config.get('username', 'j2ee')
        password = config.get('password', 'j2ee')
        login_page.page_sign_in(username, password)
        query_page.page_query(value)






