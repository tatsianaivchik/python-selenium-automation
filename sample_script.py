from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
service = Service('/Users/TANYA/QA_Automation/python-selenium-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.wait = WebDriverWait(driver, 10) #checks for condition to be net every 500ms

driver.implicitly_wait(5) # check every 100ms

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message='Search btn not clickable')

# click search
driver.find_element(By.NAME, 'btnK').click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
