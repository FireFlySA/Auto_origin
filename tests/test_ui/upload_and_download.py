import allure
from playwright.sync_api import Page

from base.pages.upload_and_download.upload_and_download_page import UploadAndDownloadPage
from base.pages.upload_and_download.upload_and_download_start import UploadStart


class TestUploadAndDownload:

    @allure.epic("Тесты потока 1")
    @allure.feature("Upload and Download")
    @allure.title("Заполнение upload_and_download формы")
    def test_upload_form(self, page: Page, upload_form: UploadAndDownloadPage):
        UploadStart.upload_and_download(page, upload_form)
