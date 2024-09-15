import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.data_picker.data_picker_methods import DataPickerMethods
from base.pages.data_picker.data_picker_page import DataPickerPage


class DataPickerStart:
    @staticmethod
    def data_picker_form(page: Page, date_picker_form: DataPickerPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.data_picker(page)

            with allure.step("Ввод данных пользователя"):
                DataPickerMethods.date_picker_fill(date_picker_form)

        except AssertionError as e:
            errors.append(str(e))
