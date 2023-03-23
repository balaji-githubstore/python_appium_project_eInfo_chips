import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "appPackage": "com.airbnb.android",
            "appActivity": "com.airbnb.android.feat.splashscreen.SplashScreenActivity"
            # "udid":"emulator-5557"
        }
        # app always get reset -- don't open any system app

        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceLocal(AppiumConfig):
    def test_invalid_login(self):
        print(self.driver.page_source)
        time.sleep(2)
