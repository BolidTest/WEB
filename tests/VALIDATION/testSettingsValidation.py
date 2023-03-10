# -*- coding: utf-8 -*-

import allure
import pytest
from selenium.webdriver.common.by import By

reruns = 1


@pytest.fixture()
def close_modal(request, app):
    def fin():
        app.method.click((By.XPATH, '(//*[.=" Отменить "]//div)[last()]'))

    request.addfinalizer(fin)


@pytest.fixture
def object(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Объект'"):
        app.PO_Navigations.goToObjectPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def date_time(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Дата и время'"):
        app.PO_Navigations.goToDateTimePage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def device(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Прибор'"):
        app.PO_Navigations.goToDevicePage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def radio(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Прибор'"):
        app.PO_Navigations.goToRadioPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def ethernet(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'ethernet'"):
        app.PO_Navigations.goToEthernetPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def light_indication(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Световая индикация'"):
        app.PO_Navigations.goToLightIndicationPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def volum_indication(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'Звуковая индикация'"):
        app.PO_Navigations.goToVolumIndicationPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()


@pytest.fixture
def GSM(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'GSM'"):
        app.PO_Navigations.goToGSMPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()
    with allure.step("Включить модуль GSM"):
        app.PO_Settings.modul_settings_gsm_on()



@pytest.fixture
def exit_enter(app):
    with allure.step("Переход на страницу Настройки"):
        app.PO_Navigations.goToSettingsPage()
    with allure.step("Переход на вкладку 'GSM'"):
        app.PO_Navigations.goToGSMPage()
    with allure.step("Клик по кнопке 'Редактировать'"):
        app.PO_Settings.edit_button_click()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test01ValidationSettings:

    @allure.story("ОБЪЕКТ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название объекта'")
    def test_input_data_name_object(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_name()

    @allure.story("ОБЪЕКТ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название объекта'")
    def test_input_data_name_object_negativ(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_name_negativ()

    @allure.story("ОБЪЕКТ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Номер объекта'")
    def test_input_data_number_object(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_number()

    @allure.story("ОБЪЕКТ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Номер объекта'")
    def test_input_data_number_object_negativ(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_number_negativ()

    @allure.story("ОБЪЕКТ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Задержка взятия'")
    def test_input_data_delay_take_object(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_delay_take()

    @allure.story("ОБЪЕКТ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Задержка взятия'")
    def test_input_data_delay_take_object_negativ(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_delay_take_negativ()

    @allure.story("ОБЪЕКТ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Задержка тревоги входа'")
    def test_input_data_delay_alarm_enter_object(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_delay_alarm_enter()

    @allure.story("ОБЪЕКТ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Задержка тревоги входа'")
    def test_input_data_delay_alarm_enter_object_negativ(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_delay_alarm_enter_negativ()

    @allure.story("ОБЪЕКТ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Время автовзятия'")
    def test_input_data_time_auto_take_on_object(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_time_auto_take_on()

    @allure.story("ОБЪЕКТ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Время автовзятия'")
    def test_input_data_time_auto_take_on_object_negativ(self, app, extend_time, object):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_object_time_auto_take_on_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test02ValidationSettings:

    @allure.story("РАДИО")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Время разрешения добавления новых датчиков'")
    def test_input_data_resolution_time_for_adding_new_sensors(self, app, extend_time, radio):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_resolution_time_for_adding_new_sensors()

    @allure.story("РАДИО")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Время разрешения добавления новых датчиков'")
    def test_input_data_resolution_time_for_adding_new_sensors_negativ(self, app, extend_time, radio):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_resolution_time_for_adding_new_sensors_negativ()

    @allure.story("РАДИО")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Период опроса датчиков'")
    def test_input_data_sensor_polling_period(self, app, extend_time, radio):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sensor_polling_period()

    @allure.story("РАДИО")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Период опроса датчиков'")
    def test_input_data_sensor_polling_period_negativ(self, app, extend_time, radio):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sensor_polling_period_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03ValidationSettings:

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Адрес сервера'")
    def test_input_data_time_server_address(self, app, extend_time, date_time):
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_time_address_server()

    @allure.story("ДАТА И ВРЕМЯ")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Адрес сервера'")
    def test_input_data_time_server_address_negativ(self, app, extend_time, date_time):
        with allure.step("Выбор: Синхронизация по NTP/HTP"):
            app.PO_Settings.Synchronization_via_NTP_HTP_click()
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_time_address_server_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test03ValidationSettings:

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'MAC адрес'")
    def test_input_data_ethernet_mac(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_mac()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'MAC адрес'")
    def test_input_data_ethernet_mac_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_mac_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Название сервера'")
    def test_input_data_ethernet_name_server(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_name_server()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Название сервера'")
    def test_input_data_ethernet_name_server_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_name_server_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Адрес IPv4'")
    def test_input_data_ethernet_ipV4_address(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_ipv4_address()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Адрес IPv4'")
    def test_input_data_ethernet_ipV4_address_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_ipv4_address_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Маска подсети'")
    def test_input_data_ethernet_subnet_mask(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_subnet_mask()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Маска подсети'")
    def test_input_data_ethernet_subnet_mask_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_subnet_mask_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Основной шлюз'")
    def test_input_data_ethernet_main_gate(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_main_gate()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Основной шлюз'")
    def test_input_data_ethernet_main_gate_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_main_gate_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test04ValidationSettings:

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Предпочтительный DNS сервер'")
    def test_input_data_ethernet_preferred_DNS_server(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_preferred_DNS_servere()

    @allure.story("ETHERNET")
    @allure.title(
        "Негативные сценарии: Проверка ввода значений в поле 'Предпочтительный DNS сервер'")
    def test_input_data_ethernet_preferred_DNS_server_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_preferred_DNS_servere_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Альтернативный DNS сервер'")
    def test_input_data_ethernet_alternative_DNS_server(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_alternative_DNS_server()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Альтернативный DNS сервер'")
    def test_input_data_ethernet_alternative_DNS_server_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_alternative_DNS_server_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Локальный IPv6 адрес'")
    def test_input_data_ethernet_local_ip_v6_address(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_local_ipv6()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Локальный IPv6 адрес'")
    def test_input_data_ethernet_local_ip_v6_address_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_local_ipv6_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Глобальный IPv6 адрес'")
    def test_input_data_ethernet_global_ip_v6_address(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_global_ipv6()

    @allure.story("ETHERNET")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Глобальный IPv6 адрес'")
    def test_input_data_ethernet_global_ip_v6_address_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_global_ipv6_negativ()

    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Предпочтительный IPv6 DNS сервер'")
    def test_input_data_ethernet_preferred_ip_v6_address(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_preferred_ipv6()

    @allure.story("ETHERNET")
    @allure.title(
        "Негативные сценарии: Проверка ввода значений в поле 'Предпочтительный IPv6 DNS сервер'")
    def test_input_data_ethernet_preferred_ip_v6_address_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_preferred_ipv6_negativ()


    @allure.story("ETHERNET")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Альтернативный IPv6 DNS сервер'")
    def test_input_data_ethernet_alternative_ip_v6_address(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_alternative_ipv6()

    @allure.story("ETHERNET")
    @allure.title(
        "Негативные сценарии: Проверка ввода значений в поле 'Альтернативный IPv6 DNS сервер'")
    def test_input_data_ethernet_alternative_ip_v6_address_negativ(self, app, extend_time, ethernet):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_ethernet_alternative_ipv6_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test05ValidationSettings:


    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Число знаков номера для проверки'")
    def test_input_data_gsm_number_of_digits_of_the_number_to_check(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_gsm_number_of_digits_of_the_number_to_check()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Число знаков номера для проверки'")
    def test_input_data_gsm_number_of_digits_of_the_number_to_check_negativ(self, app, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_gsm_number_of_digits_of_the_number_to_check_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Порог уведомления о балансе'")
    def test_input_data_gsm_balance_notification_threshold(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_gsm_balance_notification_threshold()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Порог уведомления о балансе'")
    def test_input_data_gsm_balance_notification_threshold_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_gsm_balance_notification_threshold_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_1: PIN'")
    def test_input_data_sim_1_pin(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_pin()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_1: PIN'")
    def test_input_data_sim_1_pin_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_pin_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_2: PIN'")
    def test_input_data_sim_2_pin(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_pin()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_2: PIN'")
    def test_input_data_sim_2_pin_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_pin_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_1: USSD'")
    def test_input_data_sim_1_USSD(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_USSD()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_1: USSD'")
    def test_input_data_sim_1_USSD_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_USSD_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_2: USSD'")
    def test_input_data_sim_2_USSD(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_USSD()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_2: USSD'")
    def test_input_data_sim_2_USSD_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_USSD_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test06ValidationSettings:

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_1: APN'")
    def test_input_data_sim_1_APN(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_APN()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_1: APN'")
    def test_input_data_sim_1_APN_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_APN_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_2: APN'")
    def test_input_data_sim_2_APN(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_APN()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_2: APN'")
    def test_input_data_sim_2_APN_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_APN_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_1: Пользователь'")
    def test_input_data_sim_1_user(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_user()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_1: Пользователь'")
    def test_input_data_sim_1_user_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_user_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_2: Пользователь'")
    def test_input_data_sim_2_user(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_user()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_2: Пользователь'")
    def test_input_data_sim_2_user_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_user_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_1: Пароль'")
    def test_input_data_sim_1_password(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_password()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_1: Пароль'")
    def test_input_data_sim_1_password_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_1_password_negativ()

    @allure.story("GSM")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Sim_2: Пароль'")
    def test_input_data_sim_2_password(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_password()

    @allure.story("GSM")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Sim_2: Пароль'")
    def test_input_data_sim_2_password_negativ(self, app, extend_time, GSM):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_sim_2_password_negativ()

@allure.label("owner", 'Александр Горелов')
@allure.epic("Тесты НАСТРОЙКИ")
@allure.feature("Валидация полей ввода")
@pytest.mark.flaky(reruns=reruns)
class Test07ValidationSettings:

    @allure.story("Звуковая индикация")
    @allure.title("Позитивные сценарии: Проверка ввода значений в поле 'Длительность сигнала'")
    def test_input_data_volum_indication_signal_duration(self, app, extend_time, volum_indication):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_volum_indication_signal_duration()

    @allure.story("Звуковая индикация")
    @allure.title("Негативные сценарии: Проверка ввода значений в поле 'Длительность сигнала'")
    def test_input_data_volum_indication_signal_duration_negativ(self, app, extend_time, volum_indication):
        with allure.step("Проверка валидации поля"):
            app.PO_Settings.input_data_volum_indication_signal_duration_negativ()
