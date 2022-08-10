import pytest
from settings import valid_email, valid_password, chrome_driver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(chrome_driver)
    pytest.driver.implicitly_wait(10)
    # Переходим на страницу авторизации
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


@pytest.fixture()
def go_to_my_pets():

    # Устанавливка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    """Вводим email"""
    pytest.driver.find_element_by_id('email').send_keys(valid_email)

    # Устанавливка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    """Вводим пароль"""
    pytest.driver.find_element_by_id('pass').send_keys(valid_password)

    # Устанавливка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                     'button[type="submit"]')))

    """Нажимаем на кнопку входа в аккаунт"""
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Устанавливка явного ожидания
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))

    """Нажимаем на ссылку "Мои питомцы" """
    pytest.driver.find_element_by_link_text("Мои питомцы").click()

    # Устанавливка явного ожидания
    myDynamicElement = pytest.driver.find_element_by_id("all_my_pets")