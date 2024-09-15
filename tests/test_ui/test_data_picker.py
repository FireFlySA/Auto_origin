import allure
from playwright.sync_api import Page

from base.pages.data_picker.data_picker_page import DataPickerPage
from base.pages.data_picker.data_picker_start import DataPickerStart

class TestDataPicker:

    @allure.epic("Тесты потока 1")
    @allure.feature("Data Picker")
    @allure.title("Заполнение формы Дата-пикер")
    def test_data_picker(self, page: Page, elements_data_picker: DataPickerPage):
        DataPickerStart.data_picker_form(page, elements_data_picker)
