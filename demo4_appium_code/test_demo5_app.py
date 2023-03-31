import os
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    driver = None
    app = None

    @pytest.fixture(scope='function', autouse=True)
    def config(self):
        self.app = os.getcwd() + '\\test_data\\khan-academy-7-3-2.apk'
        des_cap = {
            "platformName": "android",
            "deviceName": "pixel",
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(10)

        yield
        time.sleep(5)
        self.driver.quit()


class TestInstallKhan(AppiumConfig):
    def test_uninstall_app(self):
        if self.driver.is_app_installed("org.khanacademy.android"):
            self.driver.remove_app("org.khanacademy.android")

    def test_install_app(self):
        self.driver.install_app(self.app)
        self.driver.activate_app("org.khanacademy.android")
        # self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@text='Allow']").click()

    def test_course_challenge(self):
        self.driver.activate_app("org.khanacademy.android")

        get_dismiss_button = self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")
        if len(get_dismiss_button) > 0:
            get_dismiss_button[0].click()

        self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Search tab").click()
        # self.driver.find_element(AppiumBy.XPATH, "//android.widget.Button[@content-desc="Search tab"]").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Math']").click()

        para_dic = {"strategy": AppiumBy.ANDROID_UIAUTOMATOR, "selector": 'UiSelector().text("Class 12 math (India)")'}
        self.driver.execute_script("mobile: scroll", para_dic)
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Class 12 math (India)')]").click()

        size_dic = self.driver.get_window_size()
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        self.driver.implicitly_wait(0)
        while len(self.driver.find_elements(AppiumBy.ANDROID_UIAUTOMATOR,
                                            'UiSelector().textContains("Take Course Challenge")')) == 0:
            self.driver.swipe(x1, y1, x2, y2, 100)
        self.driver.implicitly_wait(10)

        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Take Course Challenge')]").click()

        # self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,\"Let's go\")]").click()
        # self.driver.find_element(AppiumBy.XPATH, "//android.view.View[3]").click()
        #
        # actual_text = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Give it')]").text
        # assert_that(actual_text).is_equal_to("Give it another shot!")
        # print(actual_text)

        # actual_text2 = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Try again')]").text
        # assert_that(actual_text2).is_equal_to("Try again Get help. Skip for now.")
        # print(actual_text2)

        for view in self.driver.contexts:
            print(view)
            # below code switch to webview
            self.driver.switch_to.context(view)
            if "least Kilo" in self.driver.page_source :
                break

        print(self.driver.context)