import allure
from playwright.sync_api import Page

from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.radio_button.radio_button_start import RadioButtonStart


class TestRadioButtonForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("Radio Form")
    @allure.title("Заполнение radio_button формы")
    def test_radio_button_form(self, page: Page, elements_radio_button: RadioButtonPage):
        RadioButtonStart.elements_radio_button(page, elements_radio_button)
