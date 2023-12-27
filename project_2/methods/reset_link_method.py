from selenium.webdriver.common.by import By
from project_2.Locator.Request_page import Element_request

class Request_link_sent(Element_request):
    def __init__(self, driver):
        self.driver = driver

    def verify_title_of_page(self):
        expected_title = "OrangeHRM"
        assert expected_title in self.driver.title

    def click_forgot_password_text(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.forgot_pass_button).click()
    def navigate_request_password_page(self, username):
        url_reset_page = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
        assert self.driver.current_url == url_reset_page
        print(f'current url of reset_password page: {self.driver.current_url}.')
        hd_tag = self.driver.find_element(by=By.XPATH, value=self.heading_tag).text
        print(f'this is a message for after clicking forgot_password_link :{hd_tag}.')
        assert hd_tag.__contains__(self.expected_text)
        self.driver.find_element(by=By.NAME, value=self.username_field_name).is_displayed()
        self.driver.find_element(by=By.NAME, value=self.username_field_name).send_keys(username)
        self.driver.find_element(by=By.XPATH, value=self.reset_button_xpath).click()

    def navigate_reset_link_page(self):
        password_success_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
        assert self.driver.current_url == password_success_url
        print(f'url for reset_link_page :{self.driver.current_url}.')
        self.driver.find_element(by=By.CLASS_NAME, value=self.reset_link_div_visible_class).is_displayed()
        header = self.driver.find_element(by=By.TAG_NAME, value=self.reset_link_text_xpath).text
        print(f'after passing username and clicking reset_password_button :{header}.')
