from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap={
    "app":"bs://aa104de2e2d069e729c3efae598d5a523082d186",
    "platformVersion":"9.0",
    "deviceName":"Google Pixel 3",
    "bstack:options": {
        "projectName": "First Python project",
        "buildName": "browserstack-build-1",
        "sessionName": "BStack first_test",
        # Set your access credentials
        "userName": "dinakaranbalaji1",
        "accessKey": "6yXRE4nK1fyvTHWA2kPD"
    }
}

driver=webdriver.Remote(command_executor="http://hub.browserstack.com/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

print(driver.page_source)

driver.quit()
