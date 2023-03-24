import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\Components\khan-academy-7-3-2.apk"
}

driver=webdriver.Remote(command_executor="http://localhost:4723/wd/hub",desired_capabilities=des_cap)
driver.implicitly_wait(30)

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Dismiss']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.TextView[@text='Sign in']").click()

driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[@content-desc='Enter an e-mail address or username']").send_keys("dina")
driver.find_element(AppiumBy.XPATH,"//android.widget.EditText[contains(@content-desc,'Pass')]").send_keys("dina123")

#click on sign in
driver.find_element(AppiumBy.XPATH,"(//android.widget.TextView[@text='Sign in'])[2]").click()
#get the text "There was an issue signing in" and print it

actual_error=driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'issue')]").text

print(actual_error)

actual_error=driver.find_element(AppiumBy.XPATH,"//*[contains(@text,'issue')]").get_attribute("text")

print(actual_error)

time.sleep(5)
driver.quit()
