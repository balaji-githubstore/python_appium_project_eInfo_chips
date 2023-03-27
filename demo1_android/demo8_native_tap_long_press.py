import time

import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.extensions.android.nativekey import AndroidKey

"""Touch actions """


class AppiumConfig:
    @pytest.fixture(scope="function", autouse=True)
    def handle_app_launch(self):
        des_cap = {
            "platformName": "android",
            "deviceName": "oneplus",
            "app": r"C:\Components\khan-academy-7-3-2.apk",
            "noReset": True
        }
        self.driver = webdriver.Remote(command_executor="http://localhost:4723/wd/hub", desired_capabilities=des_cap)
        self.driver.implicitly_wait(30)
        yield
        self.driver.quit()


class TestAdvanceCode(AppiumConfig):
    """Tap using co-ordinates """

    def test_tap_using_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        action = TouchAction(self.driver)
        action.tap(x=900, y=1100, count=5).perform()

        time.sleep(5)

    """Tap using webelement """

    def test_tap_using_webelement(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()
        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()
        action = TouchAction(self.driver)
        # first time find the element co-ordinates and tap 10 times
        action.tap(self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Arts and humanities']")
                   , count=10).perform()
        time.sleep(5)

    """Tap by constructing co-ordinates dynamically """

    def test_tap_using_webelement_coordinates(self):
        if len(self.driver.find_elements(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']")) > 0:
            self.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Dismiss']").click()

        self.driver.find_element(AppiumBy.ID, "org.khanacademy.android:id/tab_bar_button_search").click()

        loc = self.driver.find_element(AppiumBy.XPATH,
                                       "//android.widget.TextView[@text='Arts and humanities']").location
        print(loc)
        # 220,1070

        action = TouchAction(self.driver)
        action.tap(x=loc['x'] + 60, y=loc['y'] + 60
                   , count=10).perform()
        time.sleep(5)

    def test_long_press_coordinates(self):
        action = TouchAction(self.driver)
        action.long_press(x=330, y=1102,
                          duration=1000).perform()

    def test_long_press_webelements(self):
        time.sleep(2)
        self.driver.press_keycode(AndroidKey.HOME)
        time.sleep(2)
        self.driver.swipe(902, 1174, 902, 794, 1000)
        action = TouchAction(self.driver)
        action.long_press(self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'Khan')]"),
                          duration=1000).perform()
        self.driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'App in')]").click()

    # logics for press and move to
    def test_press(self):
        action = TouchAction(self.driver)
        action.press(100, 100).wait(1000).move_to(200, 200).release()
