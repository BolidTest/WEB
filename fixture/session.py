# -*- coding: utf-8 -*-
import time

import allure
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from locators.session_locators import *


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        with allure.step("Авторизация пользователя"):
            try:
                wd = self.app.wd
                wd.get(self.app.base_url)
                # time.sleep(1)
                self.display_and_hide((By.XPATH, authorization_window))
                self.app.method.inputValues(username, '//*[@id="username"]')
                self.app.method.inputValues(password, '//*[@id="password"]')
                self.app.method.click((By.XPATH, entry_button))
                self.login_verification()
            except:
                wd = self.app.wd
                wd.refresh()
                wd.get(self.app.base_url)
                time.sleep(1)
                self.app.method.inputValues(username, '//*[@id="username"]')
                self.app.method.inputValues(password, '//*[@id="password"]')
                self.app.method.click((By.XPATH, entry_button))
                self.login_verification()

    def login_enter(self, username, password):
        wd = self.app.wd
        wd.get(self.app.base_url)
        self.app.method.inputValues(username, '//*[@id="username"]')
        self.app.method.inputValues(password, '//*[@id="password"]')
        self.app.method.click((By.XPATH, entry_button))
        time.sleep(1)

    def logout(self):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, main_icon_button)))
            element.click()
            element1 = WebDriverWait(wd, 10).until(
                EC.element_to_be_clickable((By.XPATH, exit_button)))
            element1.click()
        except Exception as exc:
            assert exc == TimeoutException or exc == ElementClickInterceptedException, \
                f"Ошибка локатора!!! Нет возможности выйти из приложения\nЛокатор иконки выхода:'{main_icon_button}'\nЛокатор кнопки Выйти:'{exit_button}'"

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Журнал"))

    def ensure_login(self, username, password):
        self.login(username, password)

    def display_and_hide(self, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.visibility_of_element_located((locator)))
            WebDriverWait(wd, 20).until(EC.staleness_of(element))
        except Exception as e:
            assert e == TimeoutException, f"Ошибка, локатор {locator} - не найден"

    def login_verification(self):
        wd = self.app.wd
        time.sleep(3)
        assert str(wd.current_url) == str(self.app.base_url + f'/journal'), f" \n***Ошибка Входа! "