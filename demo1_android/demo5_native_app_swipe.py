import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

"""Swipe using ANDROID_UIAUTOMATOR"""


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

        # id is resource-id only
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        # ACCESSIBILITY_ID is content-desc in android
        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search tab").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']").click()

        time.sleep(5)
        # swipe until //android.widget.TextView[@text='Art of Asia'] presence
        #  self.driver.swipe(902, 1174,924, 794,1)

        # scroll to art of asia and click
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Art of Asia")'}
        self.driver.execute_script("mobile: scroll", para_dic)

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Art of Asia']").click()

        # scroll to the himalayas and click it
        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().textContains("Himala")'}
        self.driver.execute_script("mobile: scroll", para_dic)

        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().textContains("Himala")').click()
