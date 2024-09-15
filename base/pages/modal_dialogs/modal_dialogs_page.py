from playwright.async_api import Page

from base.page_factory.button import Button


class ModalDialogsPage:
    def __init__(self, page: Page)->None:
        self.page = page

        """Локаторы страницы: Модальные окна"""
        self.small_modal = Button(page, locator='//*[@id="showSmallModal"]', name='Клик на кнопку для вызова маленького модального окна')
        self.close_small_modal = Button(page, locator='//*[@id="closeSmallModal"]', name='Клик на закрытие маленькой модалки')
        self.close_modal_x = Button(page,locator='//*[@class="close"]', name='Закрытие модального окна через крестик')
        self.big_modal = Button(page, locator='//*[@id="showLargeModal"]', name='Клик на кнопку для вызова большого модального окна')
        self.close_big_modal = Button(page, locator='//*[@id="closeLargeModal"]', name='Клик на закрытие больщой модалки')
        self.close_modal_overlay = page.get_by_role('dialog')

        """Ожидания"""
        self.Wait_small_modal = '//*[@id="showSmallModal"]'
        self.Wait_big_modal = '//*[@id="showBigModal"]'