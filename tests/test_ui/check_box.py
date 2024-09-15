import allure
from playwright.sync_api import Page

from base.pages.check_box.check_box_page import CheckBoxPage
from base.pages.check_box.check_box_start import CheckBoxStart


class TestCheckBoxForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("Checkbox Form")
    @allure.title("Взаимодействие с выпадающим списком чекбоксов")
    def test_check_box(self, page: Page, check_box_form: CheckBoxPage):
        CheckBoxStart.check_box_form(page, check_box_form)