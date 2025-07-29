from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class BasePage:
    def __init__(self, driver):
        self.driver = driver  # Lưu biến driver, page con dùng lại driver này
    def wait_for_visible(self, locator, timeout=10):
        # Chờ element xuất hiện trên UI tối đa timeout giây
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    def wait_for_clickable(self, locator, timeout=10):
        # Chờ element có thể click tối đa timeout giây
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator))
    def scroll_to_text(self, text):
        """Scroll tới item có text bất kỳ (dynamic) trên Android."""
        return self.driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}"))'
        )