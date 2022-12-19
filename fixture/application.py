# -*- coding: utf-8 -*-

import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as CHROME
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options as FIREFOX

from fixture.method import MethodsHelper
from fixture.session import SessionHelper
from generator.generate_data import Ganerate
from generator.read_data import DataHelper
from pages.PO_Auth import AuthHelper
from pages.PO_Directions import DirectionsHelper
from pages.PO_Journal import JournalHelper
from pages.PO_Navigations import NavigationsHelper
from pages.PO_Sensors import SensorsHelper
from pages.PO_Settings import SettingsHelper
from pages.PO_Tooltips import TooltipsHelper
from pages.PO_Users_Keys import UsersKeysHelper
from pages.PO_Zone_Path import ZonePathHelper
from pages.PO_Status import StatusHelper
from pages.PO_Update import UpdateHelper


class Application:

    # Настройка браузеров и взаимодействие с классами помошниками
    def __init__(self, browser, base_url):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'chrome_headless':
            options = CHROME()
            options.headless = True
            self.wd = webdriver.Chrome(options=options)
            self.wd.set_window_size(1920, 1080)
        elif browser == 'chrome_no_logs':
            options = CHROME()
            options.add_experimental_option("excludeSwitches", ["enable-logging"])
            self.wd = webdriver.Chrome(options=options)
        elif browser == 'firefox_headless':
            options = FIREFOX()
            options.headless = True
            self.wd = webdriver.Firefox(options=options)
        elif browser == 'chrome_latest':
            capabilities = {"browserName": 'chrome', "browserVersion": "105.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:4444/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'chrome_99':
            capabilities = {"browserName": 'chrome', "browserVersion": "99.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:4499/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'chrome_100':
            capabilities = {"browserName": 'chrome', "browserVersion": "100.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:4100/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'chrome_101':
            capabilities = {"browserName": 'chrome', "browserVersion": "101.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://selenium:4444/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'chrome_102':
            capabilities = {"browserName": 'chrome', "browserVersion": "102.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor="http:/192.168.22.130:4102/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'firefox_101':
            capabilities = {"browserName": 'firefox', "browserVersion": "101.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:1014/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'firefox_100':
            capabilities = {"browserName": 'firefox', "browserVersion": "100.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:1004/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'firefox_98':
            capabilities = {"browserName": 'firefox', "browserVersion": "98.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:9844/wd/hub",
                                       desired_capabilities=capabilities)
        elif browser == 'firefox_99':
            capabilities = {"browserName": 'firefox', "browserVersion": "99.0", "platformName": "Linux"}
            self.wd = webdriver.Remote(command_executor=f"http://192.168.22.130:9944/wd/hub",
                                       desired_capabilities=capabilities)
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        # self.wd.set_window_size(1920, 1080)
        self.wd.implicitly_wait(10)
        self.wd.maximize_window()
        self.PO_Auth = AuthHelper(self)
        self.PO_Directions = DirectionsHelper(self)
        self.PO_Journal = JournalHelper(self)
        self.PO_Navigations = NavigationsHelper(self)
        self.PO_Settings = SettingsHelper(self)
        self.PO_Users_Keys = UsersKeysHelper(self)
        self.PO_Zone_Path = ZonePathHelper(self)
        self.PO_Tooltips = TooltipsHelper(self)
        self.PO_Sensors = SensorsHelper(self)
        self.PO_Status = StatusHelper(self)
        self.PO_Update = UpdateHelper(self)
        self.method = MethodsHelper(self)
        self.session = SessionHelper(self)
        self.read_data = DataHelper(self)
        self.ganerate_data = Ganerate(self)
        self.base_url = base_url

    # Проверка на валидный URL
    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    # Открытие домашней страницы
    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)

    # Выход из браузера
    def destroy(self):
        wd = self.wd
        self.wd.quit()

    # Выполнение скриншота для отчета Allure
    def get_screen(self):
        wd = self.wd
        # target = wd.find_element(By.XPATH, '//*[@id="modalSettings"]/div/div[2]/div[2]/button[1]')
        # actions = ActionChains(wd)
        # actions.move_to_element(target)
        # actions.perform()
        allure.attach(wd.get_screenshot_as_png(), name="↓ СКРИНШОТ ↓", attachment_type=AttachmentType.PNG)