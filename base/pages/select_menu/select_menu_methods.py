from time import sleep
import allure

from base.pages.select_menu.select_menu_page import SelectMenuPage
from settings import Settings
from src.config.expectations import Wait


class SelectMenuMethods:

    @staticmethod
    def fill_name_input(select_menu: SelectMenuPage):
        errors = []
        Wait.set_page(select_menu.page)
        try:
            with allure.step("Выбор значения первого селекта"):
                select_menu.select_value.click()
                select_menu.page.keyboard.down('Tab')
            with allure.step("Выбор значения второго селекта"):
                select_menu.select_one.click()
                select_menu.page.keyboard.down('Tab')
            with allure.step("Выбор значения третьего селекта"):
                select_menu.select_old_style.click()
                select_menu.page.keyboard.down('Tab')
            with allure.step("Выбор значения четвертого селекта"):
                select_menu.multiselect.click()
                Wait.visible(select_menu.Wait_multiselect)
                select_menu.multiselect_option_0.click()
                select_menu.multiselect_option_1.click()
                select_menu.multiselect_option_2.click()
                select_menu.multiselect_option_3.click()
                select_menu.page.keyboard.press("Tab")
            with allure.step("Выбор значения пятого селекта"):
                cars = ['volvo', 'saab', 'audi', 'opel']
                select_menu.standard_multiselect.select_option(cars)
            with allure.step('Создание скриншота'):
                screenshot_path = Settings.get_screenshot_path(file_name='select_menu.png')
                select_menu.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот')

        except AssertionError as e:
            errors.append(str(e))

