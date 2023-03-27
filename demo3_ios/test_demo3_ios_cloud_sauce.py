import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumIosConfig:
    @pytest.fixture(scope="function", autouse=True)
    def launch_app(self):
        des_cap = {
            # Set URL of the application under test
            "app": "bs://cfac38e4df65393782312425ba0ee36bf4d96247",
            # Specify device and os_version for testing
            "deviceName": "iPhone 11 Pro",
            "platformVersion": "13",
            # Set other BrowserStack capabilities
            "bstack:options": {
                "userName": "dinakaranbalaji1",
                "accessKey": "6yXRE4nK1fyvTHWA2kPD",
                "projectName": "First Python project",
                "buildName": "browserstack-build-1-ios-sauce",
                "sessionName": "BStack first_test-ios"
            }
        }

        self.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestSampleApp(AppiumIosConfig):
    def test_text_box(self):
# 3.	Enter username as john
# 4.	Enter password as john123
# 5.	Get the error message shown and assert it
