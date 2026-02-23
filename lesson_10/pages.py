from selenium.webdriver.common.by import By

class LoginPage:
    """Класс для взаимодействия co страницей авторизации."""
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def login(self, username, password):
        """
        Выполняет вход в систему c использованием логина и пароля.
        :param username: Имя пользователя.
        :param password: Пароль.
        :return: None
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

class InventoryPage:
    """Класс для взаимодействия co страницей каталога товаров."""
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_name):
        """
        Добавляет товар в корзину по ero названию.
        :param item_name: Название товара.
        :return: None
        """
        # Преобразуем название товара в ID кнопки 
        item_id = f"add-to-cart-{item_name.lower().replace(' ', '-')}"
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self):
        """
        Переходит на страницу корзины.
        :return: None
        """
        self.driver.find_element(*self.cart_link).click()

class CartPage:
    """Класс для взаимодействия co страницей корзины."""
    def __init__(self, driver):
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    def checkout(self):
        """
        Нажимает кнопку перехода к оформлению заказа.
        :return: None
        """
        self.driver.find_element(*self.checkout_button).click()

class CheckoutPage:
    """Класс для взаимодействия co страницей оформления заказа."""
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip):
        """
        Заполняет форму персональными данными и нажимает 'Continue'.
        :param first: Имя.
        :param last: Фамилия.
        :param zip: Почтовый индекс.
        :return: None
        """
        self.driver.find_element(*self.first_name).send_keys(first)
        self.driver.find_element(*self.last_name).send_keys(last)
        self.driver.find_element(*self.zip_code).send_keys(zip)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self):
        """
        Считывает итоговую сумму заказа.
        :return: Строка c итоговой ценой (например, 'Total: $58.29').
        """
        # Извлекаем текст "Total: $58.29"
        return self.driver.find_element(*self.total_label).text
