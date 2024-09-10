from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input
from src.config.expectations import Wait


class UploadAndDownloadPage(Page):
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Загрузка и скачивание файла"""
        self.download_file = Button(page, locator='//*[@id="downloadButton"]', name='Скачивание файла')
        self.picture = Input(page, locator='//*[@id="uploadFile"]', name='Загрузка файла')






