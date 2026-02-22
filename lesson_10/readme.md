Для работы Allure необходимо:

 1. Установить зависимости:
 pip install allure-python-commons
 pip install allure-pytest
 pip install pytest-allure

 2. Настроить запуск тестов:
 pytest --alluredir=allure-results tests/
 allure serve allure-results

 3. Добавить конфигурацию в pytest.ini:
[pytest]
addopts = --alluredir=allure-results

