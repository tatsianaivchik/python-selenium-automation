from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/TANYA/QA_Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")
driver.find_element(By.ID, "ap_email")
driver.find_element(By.ID, "continue")
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
driver.find_element(By.ID, "auth-fpp-link-bottom")
driver.find_element(By.ID, "ap-other-signin-issues-link")
driver.find_element(By.ID, "createAccountSubmit")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_condition_of_use')]")
driver.find_element(By.XPATH, "//a[contains(@href, 'ap_signin_notification_privacy_notice')]")






