from selenium.webdriver.common.by import By
from project_2.Locator.dashboard_page import Element_in_dashboard_page

class Main_page(Element_in_dashboard_page):

    def __init__(self, driver):
        self.driver = driver

    def select_Admin_menu(self):
        self.driver.find_element(by=By.CSS_SELECTOR, value=self.search_field).send_keys("Admin")
        self.driver.find_element(by=By.LINK_TEXT, value=self.Admin_menu).click()
        print(self.driver.current_url)
        expected_Admin_url = self.admin_url
        assert self.driver.current_url.__eq__(expected_Admin_url)
