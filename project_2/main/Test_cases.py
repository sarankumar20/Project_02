import pytest
from project_2.POM.validate_reset_link import Reset_message
from project_2.POM.validate_adimin_heder import Admin_header
from project_2.POM.validate_main_menu import Main_menu

class Test_conditions:

    @pytest.mark.usefixtures("start_and_quit")
    def test_TC_PIM_01_forgot_password_validation(self):
        Data_1 = Reset_message(self.driver)
        Data_1.verify_Reset_link()

    @pytest.mark.usefixtures("start_and_quit")
    def test_TC_PIM_02_Header_validation_Admin(self):
        Data_2 = Admin_header(self.driver)
        Data_2.verify_title_Admin_page()
        Data_2.verify_admin_nav()

    @pytest.mark.usefixtures("start_and_quit")
    def test_TC_PIM_03_Main_menu_validation_Admin(self):
        Data_3 = Main_menu(self.driver)
        Data_3.verify_main_menu()

