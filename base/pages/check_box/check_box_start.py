import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.check_box.check_box_methods import CheckBoxPageMethods
from base.pages.check_box.check_box_page import CheckBoxPage



class CheckBoxStart:
    @staticmethod
    def check_box_form(page: Page, check_box: CheckBoxPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.check_box_page(page)

            with allure.step("Раскрытие выпадающего списка с чек-боксами"):
                CheckBoxPageMethods.fill_name_input(check_box)

        except AssertionError as e:
            errors.append(str(e))
