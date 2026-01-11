from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")


    wait = WebDriverWait(driver, 10)
    wait.until(EC.text_to_be_present_in_element((By.ID, "text"), "Done!"))

    images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
    third_image_src = images[2].get_attribute("src")

    print(third_image_src)

finally:
    driver.quit()
