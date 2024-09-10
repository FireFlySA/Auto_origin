import allure
from playwright.async_api import Page

from base.pages.authorization.authorization_method import AuthorizationMethod
from base.pages.upload_and_download.upload_and_download_methods import UploadAndDownloadMethods
from base.pages.upload_and_download.upload_and_download_page import UploadAndDownloadPage



class UploadStart:
    @staticmethod
    def upload_and_download(page: Page, upload_and_download: UploadAndDownloadPage):
        errors = []
        try:
            with allure.step('открытие страницы'):
                AuthorizationMethod.upload(page)

            with allure.step('Заполнение страницы'):
                UploadAndDownloadMethods.fill_name_input(upload_and_download)

        except AssertionError as e:
            errors.append(str(e))