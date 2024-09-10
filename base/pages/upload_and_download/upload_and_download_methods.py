import allure

from base.pages.upload_and_download.upload_and_download_page import UploadAndDownloadPage
from settings import Settings
from src.config.expectations import Wait


class UploadAndDownloadMethods:

    @staticmethod
    def fill_name_input(upload:UploadAndDownloadPage):
        errors = []
        Wait.set_page(UploadAndDownloadPage)
        try:
            with allure.step('Скачивание файла'):
                upload.download_file.download_file()
            with allure.step('Загрузка файла'):
                image_path = Settings.get_media_path(file_name="sample-birch-400x300.jpg")
                upload.picture.load_file(image_path)
            with allure.step("Создание скриншота после загрузки файла"):
                screenshot_path = Settings.get_screenshot_path(file_name='uploadfile.png')
                upload.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')
        except AssertionError as e:
            errors.append(str(e))