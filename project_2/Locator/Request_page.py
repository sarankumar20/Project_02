
class Element_request:
    url_reset_page = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
    forgot_pass_button = '.orangehrm-login-forgot-header'
    rest_pass_class = 'orangehrm-card-container'
    heading_tag = '//h6[contains(@class,"forgot-password-title")]'
    expected_text = 'Reset Password'
    username_field_name = 'username'
    reset_button_xpath = '//button[contains(@class,"oxd-button--secondary")]'
    password_success_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/sendPasswordReset"
    reset_link_div_visible_class = 'orangehrm-card-container'
    reset_link_text_xpath = 'h6'
