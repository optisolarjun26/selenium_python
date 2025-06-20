from selenium import webdriver
from selenium.webdriver.common.by import By

import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

#simple alert
alert_button=driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']")
alert_button.click()
alert=driver.switch_to.alert
alert.accept()
time.sleep(5)

#ok/cancel alert
confirm_button=driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']")
confirm_button.click()
confirm=driver.switch_to.alert
confirm.dismiss()
time.sleep(5)

#prompt alert
prompt_button=driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']")    
prompt_button.click()
prompt=driver.switch_to.alert
prompt.send_keys("Test")
prompt.accept()
time.sleep(5)

driver.quit()