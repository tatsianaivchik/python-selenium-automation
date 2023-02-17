from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('/Users/TANYA/QA_Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)

driver.get('https://www.amazon.com')

# By CSS using ID
driver.find_element(By.CSS_SELECTOR, '#ap_email')

#By CSS using Class
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag')

#By CSS using multiple classes
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us.icp-nav-flag-lop')

#By CSS using attr (exept id and class)
driver.find_element(By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
#multiple attr
driver.find_element(By.CSS_SELECTOR, 'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"][tabindex="0"]')

#CSS using class and attr
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id='nav_cs_bestsellers']")

#Attr, partial match
driver.find_element(By.CSS_SELECTOR, "a.nav-a[data-csa-c-content-id*='_bestsellers']")

#CSS from parent to child
driver.find_element(By.CSS_SELECTOR, "#legalTextRow a[href*=condition_of_use]")
driver.find_element(By.CSS_SELECTOR, "div.a-section #legalTextRow a[href*=condition_of_use]")


















