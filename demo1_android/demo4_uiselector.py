import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Automation using ANDROID_UIAUTOMATOR"""
class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()

class TestLogin(AppiumConfig):
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, """UiSelector().text("Dismiss")""").click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in")').click()

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().descriptionContains("e-mail address")').send_keys("dina")

        #convert below xpath to ANDROID_UIAUTOMATOR
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'UiSelector().descriptionContains("pass")').send_keys(
            "dina123")
        # click on sign in
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("Sign in").instance(1)').click()
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("issue")').get_attribute("text")
        print(actual_error)

