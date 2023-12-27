from project_2.SRC.data import Value
from project_2.methods.dashboard import Main_page
from project_2.methods.login import Login_page
from project_2.methods.validate_Menu_bar import Display_Menus

class Main_menu:

    def __init__(self, driver):
        self.driver = driver

    def verify_main_menu(self):
        signin = Login_page(self.driver)
        signin.enter_username_field(Value.username_1)
        signin.enter_password_field(Value.password_1)
        signin.click_login_button()
        Admin = Main_page(self.driver)
        Admin.select_Admin_menu()
        menu = Display_Menus(self.driver)
        menu.verify_main_menu_display_in_admin_page_side_pan()