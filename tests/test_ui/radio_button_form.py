import allure
from playwright.sync_api import Page

from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.radio_button.radio_button_start import RadioButtonStart


class TestRadioButtonForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("radio button")
    @allure.title("Заполнение radio button формы")
    def test_radio_box(self, page: Page, elements_radio_button: RadioButtonPage):
        RadioButtonStart.elements_radio_button(page, elements_radio_button)
