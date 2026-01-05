from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/dynamicid")
    sleep(1)

  
    blue_button = driver.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']")
    blue_button.click()
    
    print("Кнопка успешно нажата.")

finally:
    sleep(3)
    driver.quit()
