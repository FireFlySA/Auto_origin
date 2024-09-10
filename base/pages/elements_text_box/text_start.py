import allure
from playwright.async_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.elements_text_box.text_box_methods import TextBoxMethods
from base.pages.elements_text_box.text_box_page import TextBoxPage


class TextStart:
    @staticmethod
    def elements_text_box(page: Page,text_box_form : TextBoxPage):
        errors = []
        try:
            with allure.step('открытие страницы'):
                AuthorizationMethod.text_box_form(page)

            with allure.step('Заполнение страницы'):
                TextBoxMethods.fill_name_input(text_box_form)

        except AssertionError as e:
            errors.append(str(e))