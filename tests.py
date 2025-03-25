# tests.py

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class StellarBurgersTests(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    # Тест успешной регистрации
    def test_successful_registration(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, REGISTER_BUTTON_MAIN_PAGE).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, REGISTRATION_FORM_NAME_INPUT)))
        
        # Заполняем форму регистрации
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_NAME_INPUT).send_keys('John Doe')
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys('johndoe@example.com')
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_PASSWORD_INPUT).send_keys('123456')
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_SUBMIT_BUTTON).click()

        # Проверяем успешность регистрации
        self.wait.until(EC.visibility_of_element_located((By.XPATH, PERSONAL_ACCOUNT_LINK)))
        personal_account_text = self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).text
        self.assertEqual(personal_account_text, 'Личный кабинет')

    # Тест ошибки при вводе короткого пароля
    def test_short_password_error(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, REGISTER_BUTTON_MAIN_PAGE).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, REGISTRATION_FORM_NAME_INPUT)))
        
        # Заполняем форму регистрации с коротким паролем
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_NAME_INPUT).send_keys('John Doe')
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_EMAIL_INPUT).send_keys('johndoe@example.com')
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_PASSWORD_INPUT).send_keys('12345')  # Пароль короче минимального
        self.driver.find_element(By.XPATH, REGISTRATION_FORM_SUBMIT_BUTTON).click()

        # Проверяем наличие ошибки
        error_message = self.driver.find_element(By.CLASS_NAME, 'error').text
        self.assertIn('Пароль должен содержать минимум 6 символов', error_message)

    # Тест входа по кнопке "Войти в аккаунт" на главной странице
    def test_login_via_main_page_button(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN_PAGE).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, LOGIN_FORM_EMAIL_INPUT)))
        
        # Заполняем форму входа
        self.driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        self.driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        self.driver.find_element(By.XPATH, LOGIN_FORM_SUBMIT_BUTTON).click()

        # Проверяем успешность входа
        self.wait.until(EC.visibility_of_element_located((By.XPATH, PERSONAL_ACCOUNT_LINK)))
        personal_account_text = self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).text
        self.assertEqual(personal_account_text, 'Личный кабинет')

    # Тест перехода в личный кабинет по клику на ссылку
    def test_personal_account_link_click(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()
        self.wait.until(EC.url_contains('/account'))

    # Тест выхода из аккаунта
    def test_logout(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN_PAGE).click()
        wait.until(EC.visibility_of_element_located((By.XPATH, LOGIN_FORM_EMAIL_INPUT)))
        
        # Вход в аккаунт
        self.driver.find_element(By.XPATH, LOGIN_FORM_EMAIL_INPUT).send_keys('existing_user@example.com')
        self.driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD_INPUT).send_keys('valid_password')
        self.driver.find_element(By.XPATH, LOGIN_FORM_SUBMIT_BUTTON).click()

        # Переходим в личный кабинет
        self.wait.until(EC.visibility_of_element_located((By.XPATH, PERSONAL_ACCOUNT_LINK)))
        self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LINK).click()

        # Нажимаем кнопку выхода
        self.driver.find_element(By.XPATH, PERSONAL_ACCOUNT_LOGOUT_BUTTON).click()

        # Проверяем успешность выхода
        self.wait.until(EC.visibility_of_element_located((By.XPATH, LOGIN_BUTTON_MAIN_PAGE)))
        login_button_text = self.driver.find_element(By.XPATH, LOGIN_BUTTON_MAIN_PAGE).text
        self.assertEqual(login_button_text, 'Войти')

    # Тест открытия раздела "Булки" в конструкторе
    def test_open_buns_section(self):
        self.driver.get(MAIN_PAGE_URL)
        self.driver.find_element(By.XPATH, BURGER_LOGO).click()
        self.wait.until(EC.visibility_of_element_located((By.XPATH, CONSTRUCTOR_BUNS_SECTION)))
        buns_section_visible = self.driver.find_element(By.XPATH, CONSTRUCTOR_BUNS_SECTION).is_displayed()
        self.assertTrue(buns_section_visible)
