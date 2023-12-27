from selenium.webdriver.common.by import By
from project_2.Locator.Adimin_page import Elements_admin

class Display_Nav_bar_items(Elements_admin):

    def __init__(self, driver):
        self.driver = driver

    def verifying_header_element_visible_or_not_span_tag(self):
        # Assuming you have a list of elements
        headers = self.driver.find_elements(by=By.XPATH, value=self.header_menu)
        # Verify if each element in the list is displayed
        for head in headers:
          if head.is_displayed():
              print(f"Element {head.text} is displayed.")
          else:
              print(f"Element {head} is not displayed.")






