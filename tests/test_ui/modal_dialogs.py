import allure
from playwright.sync_api import Page

from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.modal_dialogs.modal_dialogs_start import ModalDialogsStart

class TestModalDialogsForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("Modal Dialogs")
    @allure.title("Взаимодействие с модальными окнами")
    def test_modal_dialogs(self, page: Page, elements_modal_dialogs: ModalDialogsPage):
        ModalDialogsStart.elements_modal_dialogs(page, elements_modal_dialogs)