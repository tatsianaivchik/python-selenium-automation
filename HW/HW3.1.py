from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/TANYA/QA_Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)


driver.find_element(By.CSS_SELECTOR, 'i.a-icon.a-icon-logo')
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')
driver.find_element(By.ID, 'ap_customer_name')
driver.find_element(By.ID, 'ap_email')
driver.find_element(By.ID, 'ap_password')
driver.find_element(By.XPATH, "//div[contains(text(), 'Passwords must be')]")
driver.find_element(By.ID, 'ap_password_check')
driver.find_element(By.ID, 'continue')
driver.find_element(By.CSS_SELECTOR, 'a[href*=ap_register_notification_condition_of_use]')
driver.find_element(By.CSS_SELECTOR, 'a[href*=ap_register_notification_privacy_notice]')
driver.find_element(By.CSS_SELECTOR, 'a.a-link-emphasis[href*="/ap/signin?openid"]')
driver.find_element(By.ID, 'ab-registration-link')
