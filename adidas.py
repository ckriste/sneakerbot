from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import requests 


driver = webdriver.Firefox(executable_path='/Users/ckristek/Desktop/headlessBot/geckodriver')

driver.get("https://www.adidas.com/us/men-shoes")


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='product-CQ0022']"))
    )
finally:
    item2click = driver.find_element_by_xpath("//div[@id='product-CQ0022']")
    item2click.click()

 


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='dropdown-select   false label']"))
    )
finally:
    drop = driver.find_element_by_xpath("//div[@class='dropdown-select   false label']")
    drop.click()  

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[@title='11.5']"))
    )
finally:
    size = driver.find_element_by_xpath("//li[@title='11.5']")
    driver.execute_script("arguments[0].scrollIntoView();", size)
    hover = ActionChains(driver).move_to_element(size)
    hover.perform()
    #actions = ActionChains(driver)
    #actions.move_to_element(size).perform()
    size.click()