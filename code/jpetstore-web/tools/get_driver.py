from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

def start_Chrome(url):
    options = Options()
    browser = Options()
    # 禁用沙盒模式（增加兼容性）
    browser.add_argument('--no-sandbox')
    browser.add_experimental_option("detach", True)

    service = Service('../chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get(url)
    return driver

def quit_Chrome(driver):
    driver.quit()