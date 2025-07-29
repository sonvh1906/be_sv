from pages.be_input_otp import InputOTPLogin
from pages.be_input_phone_login import InputPhoneNumberLogin


def test_login(driver):
    input_phone_login = InputPhoneNumberLogin(driver)
    input_otp = InputOTPLogin(driver)

    input_phone_login.tap_input_phone_number()



