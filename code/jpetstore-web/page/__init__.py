from selenium.webdriver.common.by import By
#登录元素
login_btn = By.CSS_SELECTOR, '#MenuContent > a:nth-child(3)'
username = By.NAME, 'username'
password = By.NAME, 'password'
login_submit = By.NAME, 'signon'
# 查询
query_box = By.NAME, 'keyword'
query_btn = By.NAME, 'searchProducts'

#加入购物车
detail_btn = By.CSS_SELECTOR, '#Catalog > table > tbody > tr:nth-child(3) > td:nth-child(1) > a'
add_cart_btn = By.CSS_SELECTOR, '#Catalog > table > tbody > tr:nth-child(2) > td:nth-child(5) > a'
# 结账
checkout_btn = By.CSS_SELECTOR, '#Cart > a'
continue_btn = By.CSS_SELECTOR, '#Catalog > form > input[type=submit]'
confirm_btn = By.CSS_SELECTOR, '#Catalog > a'
# 检查库存
detail_btn2= By.CSS_SELECTOR, '#Catalog > table > tbody > tr:nth-child(26) > td > table > tbody > tr:nth-child(2) > td:nth-child(1) > a'