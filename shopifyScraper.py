# import requests
# from bs4 import BeautifulSoup
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
#
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.binary_location = '/Applications/Google\ Chrome\ Canary.app/Contents/MacOS/Google\ Chrome\ '
# driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"), chrome_options=chrome_options)
#
# driver.get("https://kith.com/collections/kith-monday-program")
#
#
# itemDescription = driver.find_element_by_id("product-card-info-inner")
# if itemDescription.is_displayed():
#   magnifying_glass.click()

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains





driver = webdriver.Firefox(executable_path='/Users/ckristek/Desktop/headlessBot/geckodriver')

#chrome_options = Options()
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--window-size=1366x768")

# https://sites.google.com/a/chromium.org/chromedriver/downloads
#chrome_driver = '/Users/ckristek/Desktop/headlessBot/chromedriver'

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

driver.get("https://kith.com/collections/apparel/hoody")

#itemTags = driver.find_element_by_xpath( "//div[@product-card-info-variants'][@data-product-tags']")

#itemTags = driver.find_element_by_xpath("//p[@class='product-card-meta product-card-variant']").text();

#item_list = []
#jobtitlebuttons = driver.find_elements_by_xpath("//p[@class='product-card-meta product-card-variant']")
#for job in jobtitlebuttons:
    #item_list.append(job.text)

#tagList = []
#Tagstoget = driver.find_elements_by_xpath("//div[@class='product-card-info-variants']")
#for t in Tagstoget:
    #item_list.append(t.get_attribute('data-product-tags'))


#delay = 5 # seconds

#items2Click = []
#item2click = driver.find_element_by_xpath("//a[@class='product-card-info']")



try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@class='product-card-info']"))
    )
finally:
    item2click = driver.find_element_by_xpath("//a[@class='product-card-info']")
    hover = ActionChains(driver).move_to_element(item2click)
    hover.perform()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='product-card-info-variants-item-inner'][contains(string(),'L')]"))
    )
finally:
    size = driver.find_element_by_xpath("//div[@class='product-card-info-variants-item-inner'][contains(string(),'L')]")
    hover = ActionChains(driver).move_to_element(size)
    size.click()
  

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@id='appifyCookie']"))
    )
finally:
    acceptCookie = driver.find_element_by_xpath("//button[@id='appifyCookie']")
    acceptCookie.click()
    


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn--full cart-checkout']"))
    )
finally:
    checkOut = driver.find_element_by_xpath("//button[@class='btn btn--full cart-checkout']")
    checkOut.click()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_email']"))
    )
finally:
    email = driver.find_element_by_xpath("//input[@id='checkout_email']")
    ActionChains(driver).move_to_element(email).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("test@gmail.com").perform()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_first_name']"))
     )
finally:
    first_name = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_first_name']")
    ActionChains(driver).move_to_element(first_name).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("Carter").perform()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_last_name']"))
     )
finally:
    last_name = driver.find_element_by_xpath( "//input[@id='checkout_shipping_address_last_name']" )
    ActionChains(driver).move_to_element(last_name).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("Kristek").perform()


try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_address1']"))
     )

finally:
    shipping_address = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_address1']")
    ActionChains(driver).move_to_element(shipping_address).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("517 Test Dr").perform()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_city']"))
    )

finally:
    ship_city = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_city']")
    ActionChains(driver).move_to_element(ship_city).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("Coppell").perform()

try:
    element = WebDriverWait(driver, 10).until(

        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_zip']"))

        )
finally:
        ship_zip = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_zip']")
        ActionChains(driver).move_to_element(ship_zip).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("75019").perform()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='checkout_shipping_address_phone']"))
        )

finally:
    ship_phone = driver.find_element_by_xpath("//input[@id='checkout_shipping_address_phone']")
    driver.execute_script("return arguments[0].scrollIntoView();", ship_phone)
    ActionChains(driver).move_to_element(ship_phone).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("1235674433").perform()






#email_field = browser.find_element_by_id('checkout_email')

#Creditcard_field = browser.find_element_by_id('cnb')

#ActionChains(driver).move_to_element(email_field).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("test@gmail.com").perform()

#ActionChains(driver).move_to_element(Creditcard_field).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys("1234 5698 7588 4444").perform()




#itemTags = driver.find_element_by_css_selector(".product-card-meta.product-card-variant").text
#print(item_list)
