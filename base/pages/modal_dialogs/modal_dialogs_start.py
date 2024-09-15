import allure
from playwright.async_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.modal_dialogs.modal_dialogs_method import ModalDialogsMethods
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from settings import Settings


class ModalDialogsStart:
    @staticmethod
    def elements_modal_dialogs(page: Page,modal_dialogs_form : ModalDialogsPage):
        errors = []
        try:
            with allure.step('открытие страницы'):
                AuthorizationMethod.modal_dialogs(page)

            with allure.step('Тест маленькой модалки'):
                ModalDialogsMethods.test_small_modal(modal_dialogs_form)

            with allure.step('Тест большой модалки'):
                ModalDialogsMethods.test_large_modal(modal_dialogs_form)

            with allure.step("Создание скриншота - финиш"):
                screenshot_path = Settings.get_screenshot_path(file_name='modal.png')
                page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')

        except AssertionError as e:
            errors.append(str(e))