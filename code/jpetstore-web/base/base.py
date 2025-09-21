from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self,driver):
        self.driver = driver
    #基础获取元素
    def base_get_element(self,locator,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).until(lambda x:x.find_element(*locator))
    # 点击元素
    def base_click(self,locator):
        self.base_get_element(locator).click()
    # 输入
    def base_input(self,locator,value):
        self.base_get_element(locator).clear()
        self.base_get_element(locator).send_keys(value)
    # 获取文本信息
    def base_get_text(self,locator):
        return self.base_get_element(locator).text