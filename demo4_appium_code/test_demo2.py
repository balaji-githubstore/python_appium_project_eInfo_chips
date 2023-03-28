import datetime
import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import base64

""" Store video recoding dynamically"""


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "appPackage": "org.khanacademy.android",
            "appActivity": "org.khanacademy.android.ui.library.MainActivity",
            "noReset": True
            # "udid":"emulator-5554"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        self.driver.start_recording_screen()
        yield
        encoded=self.driver.stop_recording_screen()
        da= str(datetime.datetime.now()).replace(":","-").replace("/","-")
        open(f"../recording/recording_{da}.mp4","wb").write(base64.b64decode(encoded))
        self.driver.quit()


class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        # presence of element - using length
        # if len(self.driver.find_elements(AppiumBy.ID, "//android.widget.TextView[@text='Dismiss']")) > 0:
        #     self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        self.driver.find_element(AppiumBy.XPATH,
                                 "//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys(
            "dina")
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys(
            "dina123")

        if self.driver.is_keyboard_shown():
            self.driver.hide_keyboard()

        # click on sign in
        self.driver.find_element(AppiumBy.XPATH, "(//android.widget.TextView[@text='Sign in'])[2]").click()
        # get the text "There was an issue signing in" and print it
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").text
        print(actual_error)
        actual_error = self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'issue')]").get_attribute("text")
        print(actual_error)

