from selenium.webdriver.common.by import By
from project_2.Locator.login_page import Elements_login
from project_2.SRC.data import Value
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Login_page(Elements_login):

    def __init__(self, driver):
        self.driver = driver
    try:
        def Url_verification(self):
            if self.driver.current_url == Value.homepage_url:
                print("url is matched")
                print(f'the current url of the webpage is {self.driver.current_url}')
            else:
                print("its not matched")

        def enter_username_field(self, username):
            if self.driver.current_url == Value.homepage_url:
                self.driver.find_element(by=By.NAME, value=self.username_Name).click()
                self.driver.find_element(by=By.NAME, value=self.username_Name).clear()
                self.driver.find_element(by=By.NAME, value=self.username_Name).send_keys(username)
            else:
                print("invalid credit")

        def enter_password_field(self, password):
            if self.driver.current_url == Value.homepage_url:
                self.driver.find_element(By.NAME, value=self.password_Name).click()
                self.driver.find_element(By.NAME, value=self.password_Name).clear()
                self.driver.find_element(By.NAME, value=self.password_Name).send_keys(password)
            else:
                print("no such element")

        def click_login_button(self):
            self.driver.find_element(By.XPATH, value=self.login_button_xpath).click()

    except NoSuchElementException as exception_1:
        print("no such element")
    except TimeoutException as exception_2:
        print("timeout error")
