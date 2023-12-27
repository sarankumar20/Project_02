from selenium.webdriver.common.by import By
from project_2.Locator.menu_bar import Menu_loc

class Display_Menus(Menu_loc):

    def __init__(self, driver):
        self.driver = driver
    def verify_main_menu_display_in_admin_page_side_pan(self):
        # Assuming you have a list of elements
        nav_bar_menu = self.driver.find_elements(by=By.XPATH, value=self.main_menus)
        print(f' total number of menu in main_menu :{len(nav_bar_menu)}.')
        # Verify if each element in the list is displayed
        for menu in nav_bar_menu[:8]:
            if menu.is_displayed():
                print(f"Element {menu.text} is displayed.")
            else:
                print(f"Element {menu} is not displayed.")


