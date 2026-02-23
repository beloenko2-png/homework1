import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages import LoginPage, InventoryPage, CartPage, CheckoutPage
import allure

@pytest.fixture
def driver():
    """
    Фикстура для создания и управления Firefox веб-драйвером
    
    :return: webdriver.Firefox - экземпляр Firefox драйвера
    """
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@allure.feature("E-commerce")  # Относится к функциональному блоку
@allure.story("Purchase process")  # Описание пользовательской истории
@allure.title("Проверка процесса покупки и итоговой суммы заказа")  # Название теста
@allure.description("""
Тест проверяет полный процесс покупки:
1. Авторизацию пользователя
2. Добавление товаров в корзину
3. Оформление заказа
4. Корректность итоговой суммы
""")  # Подробное описание теста
@allure.severity(allure.severity_level.NORMAL)  # Уровень критичности
def test_purchase_total(driver):
    """
    Основной тест проверки процесса покупки
    """
    with allure.step("Открытие страницы входа"):
        driver.get("https://www.saucedemo.com/")
    
    with allure.step("Авторизация пользователя"):
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавление товаров в корзину"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_to_cart("Sauce Labs Backpack")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Onesie")
        inventory_page.go_to_cart()

    with allure.step("Переход к оформлению заказа"):
        cart_page = CartPage(driver)
        cart_page.checkout()

    with allure.step("Заполнение формы доставки"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Ivan", "Ivanov", "123456")

    with allure.step("Проверка итоговой суммы заказа"):
        total_text = checkout_page.get_total()
        
        with allure.step("Верификация корректности итоговой суммы"):
            assert "58.29" in total_text, f"Ожидалась сумма $58.29, но получили {total_text}"
