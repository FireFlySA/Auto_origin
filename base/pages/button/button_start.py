import allure
from playwright.async_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.button.button_methods import ButtonMethods
from base.pages.button.button_page import ButtonPage



class ButtonStart:
    @staticmethod
    def elements_button(page: Page,button_form : ButtonPage):
        errors = []
        try:
            with allure.step('открытие страницы'):
                AuthorizationMethod.button_form(page)

            with allure.step('Заполнение страницы'):
                ButtonMethods.fill_name_input(button_form)

        except AssertionError as e:
            errors.append(str(e))