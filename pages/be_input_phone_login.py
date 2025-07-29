from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import BasePage


class InputPhoneNumberLogin(BasePage):
    INPUT_PHONE_NUMBER = (AppiumBy.ID,'xyz.be.driver:id/input_phone_number')
    BUTTON_NEXT_PHONE = (AppiumBy.ID,'xyz.be.driver:id/label_next')


    def tap_input_phone_number(self):
        self.wait_for_clickable(self.INPUT_PHONE_NUMBER).click()
    def enter_phone_number(self):
        return self.wait_for_clickable(self.INPUT_PHONE_NUMBER).send_keys('0903660810')
    def tap_button_next(self):
        self.wait_for_clickable(self.BUTTON_NEXT_PHONE).click()
    def tap_otp_boxes(self):
        self.wait_for_clickable(self.BUTTON_OTP_BOXES).click()
    def enter_otp(self):
        return self.wait_for_clickable(self.BUTTON_OTP_BOXES).send_keys('4')
