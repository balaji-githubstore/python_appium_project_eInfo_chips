import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Swipe using appium default method"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            # "automationName":"UiAutomator2"
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestArts(AppiumConfig):
    def test_the_himalayas_topics(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        time.sleep(5)
        self.driver.implicitly_wait(0)

        # swipe until //android.widget.TextView[@text='Art of Asia'] presence
        # len(self.driver.find_elements) - if it 0 then element is not present
        # swipe when length is zero otherwise it comes out of while loop
        while len(self.driver.find_elements(AppiumBy.XPATH, "//*[@text='Art of Asia']")) == 0:
            self.driver.swipe(902, 1174, 902, 794, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@text='Art of Asia']").click()

        self.driver.implicitly_wait(30)
        time.sleep(5)
        # will start at 11:30 AM IST
