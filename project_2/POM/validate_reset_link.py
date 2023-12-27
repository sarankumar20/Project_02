from project_2.methods.reset_link_method import Request_link_sent
from project_2.SRC.data import Value

class Reset_message(Value):

    def __init__(self,driver):
        self.driver = driver

    def verify_Reset_link(self):
        reset = Request_link_sent(self.driver)
        reset.verify_title_of_page()
        reset.click_forgot_password_text()
        reset.navigate_request_password_page(self.username_1)
        reset.navigate_reset_link_page()