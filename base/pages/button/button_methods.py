import allure

from base.pages.button.button_page import ButtonPage
from settings import Settings


class ButtonMethods:

    @staticmethod
    def fill_name_input(elements_button:ButtonPage):
        errors = []
        try:
            with allure.step("Двойной клик"):
                elements_button.double_click.double_click()
            with allure.step("Клик правой кнопкой мыши"):
                elements_button.right_click.right_click()
            with allure.step("Клик"):
                elements_button.click.click()
            with allure.step("Создание скриншота"):
                screenshot_path = Settings.get_screenshot_path(file_name='button.png')
                elements_button.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')
        except AssertionError as e:
            errors.append(str(e))