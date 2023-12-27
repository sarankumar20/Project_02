from project_2.SRC.data import Value
from project_2.methods.dashboard import Main_page
from project_2.methods.login import Login_page
from project_2.methods.validate_admin import Display_Nav_bar_items

class Admin_header:
    def __init__(self, driver):
        self.driver = driver
    def verify_title_Admin_page(self):
        expected_title = 'OrangeHRM'
        assert expected_title in self.driver.title
    def verify_admin_nav(self):
        signin = Login_page(self.driver)
        signin.Url_verification()
        signin.enter_username_field(Value.username_1)
        signin.enter_password_field(Value.password_1)
        signin.click_login_button()
        search = Main_page(self.driver)
        search.select_Admin_menu()
        admin = Display_Nav_bar_items(self.driver)
        admin.verifying_header_element_visible_or_not_span_tag()