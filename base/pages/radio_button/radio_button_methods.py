import allure

from base.pages.radio_button.radio_button_page import RadioButtonPage
from settings import Settings


class RadioButtonMethods:

    @staticmethod
    def fill_name_input(elements_radio_button:RadioButtonPage):
        errors = []
        try:
            with allure.step("Выбор значения Yes"):
                elements_radio_button.yes.click()
            with allure.step("Создание скриншота"):
                screenshot_path = Settings.get_screenshot_path(file_name='yes.png')
                elements_radio_button.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот выбора yes')
            with allure.step("Выбор значения Impressive"):
                elements_radio_button.impressive.click()
            with allure.step("Создание скриншота 2"):
                screenshot_path = Settings.get_screenshot_path(file_name='impressive.png')
                elements_radio_button.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот выбора impressive')
        except AssertionError as e:
            errors.append(str(e))