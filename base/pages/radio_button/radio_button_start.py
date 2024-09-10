import allure
from playwright.async_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.radio_button.radio_button_methods import RadioButtonMethods
from base.pages.radio_button.radio_button_page import RadioButtonPage


class RadioButtonStart:
    @staticmethod
    def elements_radio_button(page: Page,radio_button_form : RadioButtonPage):
        errors = []
        try:
            with allure.step('открытие страницы'):
                AuthorizationMethod.radio_button_form(page)

            with allure.step('Заполнение страницы'):
                RadioButtonMethods.fill_name_input(radio_button_form)

        except AssertionError as e:
            errors.append(str(e))