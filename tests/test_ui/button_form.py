import allure
from playwright.sync_api import Page

from base.pages.button.button_page import ButtonPage
from base.pages.button.button_start import ButtonStart


class TestButtonForm:

    @allure.epic("Тесты потока 1")
    @allure.feature("Button Form")
    @allure.title("Заполнение button формы")
    def test_button_form(self, page: Page, elements_button: ButtonPage):
        ButtonStart.elements_button(page, elements_button)
