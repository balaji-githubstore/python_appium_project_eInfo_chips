import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that

""" Web APP"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "browserName": "Chrome",
            "chromedriverExecutable": r"C:\Components\chromedriver_win32 (6)\chromedriver.exe"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        self.driver.get("https://google.com")
        yield
        self.driver.quit()


class TestAndroidDeviceLocal(AppiumConfig):
    def test_title(self):
        assert_that("Google").is_equal_to(self.driver.title)

    def test_gmail(self):
        self.driver.find_element(AppiumBy.XPATH,"//span[text()='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@id='identifierId']").send_keys("hello")
        time.sleep(5)
