import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "app": "bs://aa104de2e2d069e729c3efae598d5a523082d186",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "bstack:options": {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": "dinakaranbalaji1",
                "accessKey": "6yXRE4nK1fyvTHWA2kPD"
            }
        }
        self.driver = webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",
                                       desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAndroidDeviceCloud(AppiumConfig):

    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Sign in']").click()
        print(self.driver.page_source)

    def test_invalid_sign_up_email_test(self):
        self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        #click on setting icon
        #click on sign in
        #click on sign up with email
        #send firstnamea as john
        #send lastname as peter
        #send birthday Aug 20, 1995
        #send password as welcome123
        #send email as test123
        #click on create
        #assert the error message of mail id


