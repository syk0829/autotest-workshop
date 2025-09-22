import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import os

# 读取配置文件
def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'settings.json')
    with open(config_path, 'r') as f:
        return json.load(f)
@pytest.fixture(scope="session")
def config():
    """加载配置信息"""
    return load_config()

@pytest.fixture(scope="function")  # 每个测试方法都会创建新的driver
def driver(config):
    """创建和管理WebDriver实例"""
    options = Options()

    # 从配置文件读取浏览器选项
    browser_options = config.get('browser_options', {})
    if browser_options.get('headless', False):
        options.add_argument('--headless')
    if browser_options.get('no_sandbox', True):
        options.add_argument('--no-sandbox')
    if browser_options.get('disable_dev_shm_usage', True):
        options.add_argument('--disable-dev-shm-usage')

    # 使用webdriver-manager自动管理驱动
    service = Service("../chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    # 设置超时和窗口
    driver.implicitly_wait(config.get('implicit_wait', 10))
    if config.get('maximize_window', True):
        driver.maximize_window()

    yield driver

    # 清理：关闭driver
    driver.quit()


@pytest.fixture(scope="class")  # 类级别的driver，适用于需要保持状态的测试
def class_driver(config):
    """类级别的WebDriver实例，用于需要保持状态的测试序列"""
    options = Options()

    browser_options = config.get('browser_options', {})
    if browser_options.get('headless', False):
        options.add_argument('--headless')
    if browser_options.get('no_sandbox', True):
        options.add_argument('--no-sandbox')
    if browser_options.get('disable_dev_shm_usage', True):
        options.add_argument('--disable-dev-shm-usage')

    service = Service("../chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=options)

    driver.implicitly_wait(config.get('implicit_wait', 10))
    if config.get('maximize_window', True):
        driver.maximize_window()

    # 导航到基础URL
    driver.get(config.get('base_url'))

    yield driver

    driver.quit()