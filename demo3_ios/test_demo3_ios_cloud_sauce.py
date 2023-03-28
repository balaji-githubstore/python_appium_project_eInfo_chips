import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from assertpy import assert_that


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
    def test_invalid_login(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("admin")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "admin123")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()
        actual_error = self.driver.find_element(AppiumBy.XPATH,
                                                "//XCUIElementTypeStaticText[contains(@name,'not match')]").text
        assert_that(actual_error).contains("Username and password do not match")

    def test_add_to_cart_method1(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_method2(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())

        size_dic = self.driver.get_window_size()
        x1 = size_dic['width'] * (50 / 100)
        y1 = size_dic['height'] * (75 / 100)

        x2 = size_dic['width'] * (50 / 100)
        y2 = size_dic['height'] * (25 / 100)

        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.swipe(x1, y1, x2, y2, 1000)

        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_mobile_command_method3(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()
        # swipe and click on checkout
        print(len(self.driver.find_elements(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']")))
        print(self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed())

        # swipe based on visiblity
        while not self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").is_displayed():
            self.driver.execute_script("mobile: scroll", {"direction": "down"})

        # self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()

    def test_add_to_cart_mobile_command_method4(self):
        self.driver.find_element(AppiumBy.NAME, "test-Username").send_keys("standard_user")
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeSecureTextField[@name='test-Password']").send_keys(
            "secret_sauce")
        self.driver.find_element(AppiumBy.IOS_PREDICATE, "name=='test-LOGIN'").click()

        # add to cart 4 items
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()
        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-ADD TO CART']").click()

        self.driver.find_element(AppiumBy.XPATH, "//XCUIElementTypeOther[@name='test-Cart']").click()

        para_dic = {"direction": "down", "predicateString": "name=='Terms of Service | Privacy Policy'", "toVisible": True}
        self.driver.execute_script("mobile: scroll", para_dic)
        # self.driver.execute_script("mobile: scroll", {"direction": "down"})
        self.driver.find_element(AppiumBy.XPATH, "//*[@name='test-CHECKOUT']").click()