import pytest
from selenium import webdriver
from calculator_page import CalculatorPage
import allure

@pytest.fixture
def driver():
    """
    Фикстура для создания веб-драйвера
    
    :return: webdriver.Chrome - драйвер Chrome
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@allure.feature("Калькулятор")  # Функциональный блок
@allure.story("Выполнение вычислений")  # Пользовательская история
@allure.title("Проверка работы медленного калькулятора")  # Название теста
@allure.description("""
Тест проверяет корректность работы калькулятора с задержкой:
- Установка задержки 45 секунд
- Выполнение операции 7 + 8
- Проверка результата
""")  # Подробное описание
@allure.severity(allure.severity_level.BLOCKER)  # Уровень критичности
def test_slow_calculator(driver):
    """
    Основной тест проверки калькулятора
    """
    with allure.step("Открытие страницы калькулятора"):
        page = CalculatorPage(driver)
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установка задержки 45 секунд"):
        page.set_delay("45")

    with allure.step("Выполнение математической операции"):
        page.click_button("7")
        page.click_button("+")
        page.click_button("8")
        page.click_button("=")

    with allure.step("Получение и проверка результата"):
        result = page.get_result(50)
        
        with allure.step("Верификация полученного результата"):
            assert result == "15", f"Ожидалось 15, но получено {result}"


