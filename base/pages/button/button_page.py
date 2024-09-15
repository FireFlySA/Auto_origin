from playwright.async_api import Page

from base.page_factory.button import Button


class ButtonPage:
    def __init__(self, page: Page)->None:
        self.page = page

        """Локаторы страницы: Кнопки"""
        self.double_click = Button(page, locator='//*[@id="doubleClickBtn"]', name='Двойной клик')
        self.right_click = Button(page, locator='//*[@id="rightClickBtn"]', name='Клик правой кнопкой мыши')
        self.click = page.locator('(//*[starts-with(@class, "btn")])').get_by_text("Click Me", exact=True)