import pytest
from selenium import webdriver
from calculator_page import CalculatorPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_slow_calculator(driver):
    page = CalculatorPage(driver)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    page.set_delay("45")
    
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    # Ждем результат 
    result = page.get_result(50)

    assert result == "15", f"Ожидалось 15, но получено {result}"
