import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:app": "/Users/son.vo/Desktop/app.apk",
        "appium:appWaitActivity": "*.*"
    })
    driver = webdriver.Remote('http://localhost:4723', options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

