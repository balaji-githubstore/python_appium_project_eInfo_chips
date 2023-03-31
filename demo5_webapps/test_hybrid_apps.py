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
            # "app": r"C:\Components\myTS_1.3_apkcombo.com.apk",
            "chromedriverExecutable": r"C:\Components\chromedriver_win32 (6)\chromedriver.exe",
            "appPackage": "com.ltts.myts",
            "appActivity": "android.support.customtabs.trusted.LauncherActivity"
        }

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceLocal(AppiumConfig):
    # def test_login(self):
    #     print(self.driver.contexts)
    #     for context in self.driver.contexts:
    #         self.driver.switch_to.context(context)
    #         if len(self.driver.find_elements(AppiumBy.XPATH,"//*[@type='email']"))>0:
    #             break
    #
    #     self.driver.find_element(AppiumBy.XPATH,"//*[@type='email']").send_keys("44545")
    #     self.driver.find_element(AppiumBy.XPATH,"//*[@type='submit']").click()

    def test_hybrid_app(self):
        # list[str]
        print(self.driver.contexts)

        # for loop identifies given xpath is in web view or native view
        for view in self.driver.contexts:
            print(view)
            # below code switch to webview
            self.driver.switch_to.context(view)
            if len(self.driver.find_elements(AppiumBy.XPATH, "//*[@type='email']")) > 0:
                break

        #now driver will point to the view where xpath is present
        self.driver.find_element(AppiumBy.XPATH, "//*[@type='email']").send_keys("33444")
        self.driver.find_element(AppiumBy.XPATH, "//*[@type='submit']").click()

        # switch to native view by providing the xpath
        # for view in self.driver.contexts:
        #     print(view)
        #     self.driver.switch_to.context(view)
        #     if len(self.driver.find_elements(AppiumBy.XPATH,""))>0:
        #         break

    def test_hybrid_app2(self):
        # list[str] - all view in current screen
        print(self.driver.contexts)

        #driver pointing which view
        print(self.driver.context)

        self.driver.switch_to.context("WEBVIEW_chrome")

        # driver pointing which view
        print(self.driver.context)

        self.driver.find_element(AppiumBy.XPATH, "//*[@type='email']").send_keys("33444")
        self.driver.find_element(AppiumBy.XPATH, "//*[@type='submit']").click()
