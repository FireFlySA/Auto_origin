import allure
from playwright.sync_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.select_menu.select_menu_methods import SelectMenuMethods
from base.pages.select_menu.select_menu_page import SelectMenuPage


class SelectMenuStart():
    @staticmethod
    def select_menu(page: Page, select_menu: SelectMenuPage):
        errors = []
        try:
            with allure.step("Открытие страницы"):
                AuthorizationMethod.auth_select_menu(page)

            with allure.step("Ввод данных пользователя"):
                SelectMenuMethods.fill_name_input(select_menu)

        except AssertionError as e:
            errors.append(str(e))
