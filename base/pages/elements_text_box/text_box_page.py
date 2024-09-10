from playwright.async_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class TextBoxPage:
    def __init__(self, page: Page)->None:
        self.page = page

        """Локаторы страницы Text Box"""
        self.full_name = Input(page, locator='//*[@id="userName"]', name='Полное имя')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='почта')
        self.current_address = Input(page, locator='//*[@id="currentAddress"]', name='Текущий адрес')
        self.permanent_address = Input(page, locator='//*[@id="permanentAddress"]', name='Постоянный адрес')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Кнопка сабмита')