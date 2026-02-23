from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    """Класс для взаимодействия co страницей калькулятора."""

    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def set_delay(self, seconds):
        """
        Устанавливает значение задержки выполнения операций.
        :param seconds: Время задержки в секундах (строка).
        :return: None
        """

        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(seconds)

    def click_button(self, text):
        """
        Находит и кликает по кнопке калькулятора по её тексту.
        :param text: Текст на кнопке (например, '7', '+', '=').
        :return: None
        """
        button_xpath = f"//span[text()='{text}']"
        self.driver.find_element(By.XPATH, button_xpath).click()

    def get_result(self, timeout):
        """
        Ожидает появления конкретного результата (15) и возвращает текст экрана.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Текстовое значение, отображаемое на экране калькулятора (str).
        """
        
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, "15")
        )
        return self.driver.find_element(*self.screen).text
