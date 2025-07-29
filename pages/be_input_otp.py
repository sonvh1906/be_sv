from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class InputOTPLogin(BasePage):
    BUTTON_OTP_BOXES = (AppiumBy.XPATH, '//android.widget.EditText')

    def tap_input_otp(self):
        self.wait_for_clickable(self.BUTTON_OTP_BOXES).click()

    def input_otp(self):
        self.wait_for_clickable(self.BUTTON_OTP_BOXES).send_keys('4')
