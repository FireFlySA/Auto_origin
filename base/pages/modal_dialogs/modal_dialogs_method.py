import allure

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from settings import Settings


class ModalDialogsMethods:

    @staticmethod
    def test_small_modal(elements_modal_dialogs:ModalDialogsPage):
        errors = []
        try:
            with allure.step("Клик на кнопку для вызова маленького модального окна"):
                elements_modal_dialogs.small_modal.click()
            with allure.step("Создание скриншота открытой модалки"):
                screenshot_path = Settings.get_screenshot_path(file_name='smallmodal.png')
                elements_modal_dialogs.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')
            with allure.step("Закрытие модального окна кнопкой"):
                elements_modal_dialogs.close_small_modal.click()
            with allure.step("Клик на кнопку для вызова маленького модального окна"):
                elements_modal_dialogs.small_modal.click()
            with allure.step("Закрытие модального окна через крестик"):
                elements_modal_dialogs.close_modal_x.click()
            with allure.step("Клик на кнопку для вызова маленького модального окна"):
                elements_modal_dialogs.small_modal.click()
            with allure.step("Закрытие модального окна вне элемента"):
                elements_modal_dialogs.close_modal_overlay.click()
            with allure.step("Клик на кнопку для вызова маленького модального окна"):
                elements_modal_dialogs.small_modal.click()
            with allure.step("Закрытие модального окна через esc"):
                elements_modal_dialogs.page.keyboard.press('Escape')
        except AssertionError as e:
            errors.append(str(e))

    @staticmethod
    def test_large_modal(elements_modal_dialogs: ModalDialogsPage):
        errors = []
        try:
            with allure.step("Клик на кнопку для вызова большого модального окна"):
                elements_modal_dialogs.big_modal.click()
            with allure.step("Создание скриншота открытой модалки"):
                screenshot_path = Settings.get_screenshot_path(file_name='bigmodal.png')
                elements_modal_dialogs.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')
            with allure.step("Закрытие модального окна кнопкой"):
                elements_modal_dialogs.close_big_modal.click()
            with allure.step("Клик на кнопку для вызова большого модального окна"):
                elements_modal_dialogs.big_modal.click()
            with allure.step("Закрытие модального окна через крестик"):
                elements_modal_dialogs.close_modal_x.click()
            with allure.step("Клик на кнопку для вызова большого модального окна"):
                elements_modal_dialogs.big_modal.click()
            with allure.step("Закрытие модального окна вне элемента"):
                elements_modal_dialogs.close_modal_overlay.click()
            with allure.step("Клик на кнопку для вызова большого модального окна"):
                elements_modal_dialogs.big_modal.click()
            with allure.step("Закрытие модального окна через esc"):
                elements_modal_dialogs.page.keyboard.press('Escape')
        except AssertionError as e:
            errors.append(str(e))