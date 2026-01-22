from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def test_slow_calculator():
    # Настройка драйвера Chrome
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # Увеличиваем время ожидания до 50 секунд, так как калькулятор считает 45 секунд
    wait = WebDriverWait(driver, 50)

    try:
        # 1. Открытие страницы
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        # 2. Ввод задержки 45 секунд
        delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
        delay_input.clear()
        delay_input.send_keys("45")

        # 3. Нажатие кнопок: 7, +, 8, =
        # Используем поиск по тексту на кнопках (тег span)
        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        # 4. Проверка результата 15 через 45 секунд
        # Ждем, пока в элементе с классом screen появится текст "15"
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )

        # Дополнительная проверка через assert
        final_result = driver.find_element(By.CLASS_NAME, "screen").text
        assert final_result == "15", f"Ожидалось 15, но получили {final_result}"

    finally:
        # Закрытие браузера
        driver.quit()

if __name__ == "__main__":
    test_slow_calculator()
