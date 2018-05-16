from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = driver.command_executor._url
session_id = driver.session_id

driver = webdriver.Remote(command_executor=url,desired_capabilities={})
driver.session_id = session_id

driver.get("http://www.mrsmart.in")
