from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

def test_saucedemo_shop():
    # Настройка драйвера Firefox
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открыть сайт
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # 3. Добавление товаров в корзину
        # Используем селекторы для добавления конкретных товаров
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

        # 4. Перейти в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # 5. Нажать Checkout
        driver.find_element(By.ID, "checkout").click()

        # 6. Заполнение формы данными
        driver.find_element(By.ID, "first-name").send_keys("Иван")
        driver.find_element(By.ID, "last-name").send_keys("Петров")
        driver.find_element(By.ID, "postal-code").send_keys("123456")

        # 7. Нажать Continue
        driver.find_element(By.ID, "continue").click()

        # 8. Чтение итоговой стоимости
        # Ищем элемент, содержащий итоговую сумму (Total: $58.29)
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text  # Получаем строку вида "Total: $58.29"

        # 10. Проверка (assert), что итоговая сумма равна $58.29
        # Проверяем вхождение нужной суммы в текст элемента
        assert "$58.29" in total_text, f"Ожидалась сумма $58.29, но получили {total_text}"

    finally:
        # 9. Закрыть браузер
        driver.quit()

if __name__ == "__main__":
    test_saucedemo_shop()
