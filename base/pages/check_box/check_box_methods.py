from time import sleep
import allure

from base.pages.check_box.check_box_page import CheckBoxPage
from settings import Settings
from src.config.expectations import Wait


class CheckBoxPageMethods:

    @staticmethod
    def fill_name_input(check_box: CheckBoxPage):
        errors = []
        Wait.set_page(check_box.page)
        try:
            with allure.step("Раскрытие списка с чек-боксами"):
                check_box.first_button.click()
                check_box.second_button.click()
                check_box.third_button.click()
                check_box.fourth_button.click()
                check_box.fifth_button.click()
                check_box.sixth_button.click()
                check_box.angular_button.click()
                check_box.private_button.click()
                check_box.word_file_button.click()
                check_box.commands_button.click()

            with allure.step("Создание скриншота с развернутым меню и отмеченными чек-боксами"):
                screenshot_path = Settings.get_screenshot_path(file_name='check_box_1.png')
                check_box.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот развернутого меню')

            with allure.step("Закрытие списка с чек-боксами"):
                check_box.collapse_all_button.click()

            with allure.step("Создание скриншота свернутого меню"):
                screenshot_path = Settings.get_screenshot_path(file_name='check_box_2.png')
                check_box.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот свернутого меню')


        except AssertionError as e:
            errors.append(str(e))
