
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()

#By XPath, tag attribute
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

#By XPath, multiple attr
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @data-csa-c-id='lb2yi1-c7c8da-88c5jg-f6dr0e']")

#By XPath, contains:
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers')]")

#contains AND attr
driver.find_element(By.XPATH, "//a[contains(@href, '/gp/bestsellers') and @data-csa-c-type='link']")

#for XPath without tag
driver.find_element(By.XPATH, "//*[contains(@href, '/gp/bestsellers') and @data-csa-c-type='link']")
driver.find_element(By.XPATH, "//*[contains(@href, '/gp/bestsellers')]")

# By Xpath, text
driver.find_element(By.XPATH, "//h2[text()='The warm-weather edit']")

#By XPath, contains text
driver.find_element(By.XPATH, "//h2[contains(text(), 'The warm-weather edit')]")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

#By XPath, going from parent node ==> child
driver.find_element(By.XPATH, "//div[@id='nav-xshop']//a[text()='Best Sellers']")
