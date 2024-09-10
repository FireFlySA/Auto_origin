import allure
from playwright.sync_api import Page

from base.pages.elements_text_box.text_box_page import TextBoxPage
from base.pages.elements_text_box.text_start import TextStart
from conftest import elements_text_box

class TestBoxForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("Text Box Form")
    @allure.title("Заполнение text-box формы")
    def test_text_box_form(self, page: Page, elements_text_box: TextBoxPage):
        TextStart.elements_text_box(page, elements_text_box)
