from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/classattr")
      
    sleep(4)
   
    blue_button = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    blue_button.click()
  
    sleep(4)
    alert = driver.switch_to.alert
    alert.accept()
    print("Кнопка успешно нажата.")

finally:
    sleep(4)
    driver.quit()
