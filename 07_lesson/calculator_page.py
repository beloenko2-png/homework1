from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text):
        button_xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, button_xpath).click()

    def get_result(self, timeout):
        # Ожидание
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text
