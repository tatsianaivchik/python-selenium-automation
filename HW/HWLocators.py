from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/TANYA/QA_Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


# driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
# driver.find_element(By.ID, "ap_email")
# driver.find_element(By.ID, "continue")
# driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
# driver.find_element(By.ID, "auth-fpp-link-bottom")
# driver.find_element(By.ID, "ap-other-signin-issues-link")
# driver.find_element(By.ID, "createAccountSubmit")
# driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
# driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")


driver.get('https://www.amazon.com')

driver.find_element(By.ID, "nav-orders").click()
expected_result = "Sign in"
actual_result = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

assert expected_result == actual_result, f'Expected {expected_result} but got {actual_result}'
assert driver.find_element(By.ID, 'ap_email').is_displayed(), 'Email field was not found'

driver.quit()