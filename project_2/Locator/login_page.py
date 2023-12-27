from selenium.webdriver.common.by import By

class Elements_login:
    Base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    fp_butt = (By.CSS_SELECTOR, '.orangehrm-login-forgot-header')
    username_Name = "username"
    password_Name = "password"
    login_button_xpath = '//button[text()=" Login "]'
    search_bar_path = (By.XPATH, '//input[@class="oxd-input oxd-input--active"]')
    admin_butt = (By.LINK_TEXT, 'Admin')
    admin_page_heading = (By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')