import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage

@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_purchase_total(driver):
    driver.get("https://www.saucedemo.com/")
    
    # Авторизация
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # Добавление 
    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    inventory_page.add_to_cart("Sauce Labs Onesie")
    inventory_page.go_to_cart()

    # Переход к оформлению
    cart_page = CartPage(driver)
    cart_page.checkout()

    # Заполнение данных
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Ivan", "Ivanov", "123456")

    # Проверка итоговой суммы
    total_text = checkout_page.get_total()
    assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получили {total_text}"
