from playwright.sync_api import Page

from base.base import BasePage
from src.config.url import Url


class AuthorizationMethod:

    @staticmethod
    def auth_practice_form(page: Page):
        BasePage.open_page(page, Url.AUTOMATION_PRACTICE_FORM)

    @staticmethod
    def text_box_form(page: Page):
        BasePage.open_page(page, Url.TEXT_BOX)

    @staticmethod
    def radio_button_form(page: Page):
        BasePage.open_page(page, Url.RADIO_BUTTON)

    @staticmethod
    def auth_select_menu(page: Page):
        BasePage.open_page(page, Url.SELECT_MENU)

    @staticmethod
    def button_form(page: Page):
        BasePage.open_page(page, Url.BUTTONS)

    @staticmethod
    def upload(page: Page):
        BasePage.open_page(page, Url.UPLOAD_DOWNLOAD)

    @staticmethod
    def modal_dialogs(page: Page):
        BasePage.open_page(page, Url.MODAL_DIALOGS)

    @staticmethod
    def data_picker(page: Page):
        BasePage.open_page(page, Url.DATE_PICKER)

    @staticmethod
    def check_box_page(page: Page):
        BasePage.open_page(page, Url.CHECK_BOX)