from playwright.async_api import Page

from base.page_factory.input import Input


class RadioButtonPage:
    def __init__(self, page: Page)->None:
        self.page = page

        """Локаторы страницы: Радио-кнопки"""
        self.yes = Input(page, locator= '//*[@for="yesRadio"]', name='yes')
        self.impressive = Input(page, locator='//*[@for="impressiveRadio"]', name='impressive')