import pytest

from base.pages.button.button_page import ButtonPage
from base.pages.check_box.check_box_page import CheckBoxPage
from base.pages.data_picker.data_picker_page import DataPickerPage
from base.pages.elements_text_box.text_box_page import TextBoxPage
from base.pages.modal_dialogs.modal_dialogs_page import ModalDialogsPage
from base.pages.practice_form.practice_form_page import PracticeFormPage
from base.pages.radio_button.radio_button_page import RadioButtonPage
from base.pages.select_menu.select_menu_page import SelectMenuPage
from base.pages.upload_and_download.upload_and_download_page import UploadAndDownloadPage
from src.config.playwright import PlaywrightConfig
from playwright.sync_api import Page, sync_playwright, Browser


@pytest.fixture()
def page() -> Page:
    with sync_playwright() as playwright:
        browser = get_browser(playwright)
        page = browser.new_page(viewport=PlaywrightConfig.PAGE_VIEWPORT_SIZE)
        yield page
        browser.close()


def get_browser(playwright) -> Browser:
    browser_type = playwright.chromium if PlaywrightConfig.BROWSER == 'chrome' else playwright.firefox
    return browser_type.launch(
        headless=PlaywrightConfig.IS_HEADLESS,
        slow_mo=PlaywrightConfig.SLOW_MO
    )


@pytest.fixture(scope='function')
def practice_form(page: Page) -> PracticeFormPage:
    return PracticeFormPage(page)

@pytest.fixture(scope='function')
def elements_text_box(page: Page) -> TextBoxPage:
    return TextBoxPage(page)

@pytest.fixture(scope='function')
def elements_radio_button(page: Page) -> RadioButtonPage:
    return RadioButtonPage(page)

@pytest.fixture(scope='function')
def elements_button(page: Page) -> ButtonPage:
    return ButtonPage(page)

@pytest.fixture(scope='function')
def select_menu(page: Page) -> SelectMenuPage:
    return SelectMenuPage(page)

@pytest.fixture(scope='function')
def upload_form(page: Page) -> UploadAndDownloadPage:
    return UploadAndDownloadPage(page)

@pytest.fixture(scope='function')
def elements_modal_dialogs(page: Page) -> ModalDialogsPage:
    return ModalDialogsPage(page)

@pytest.fixture(scope='function')
def elements_data_picker(page: Page) -> DataPickerPage:
    return DataPickerPage(page)

@pytest.fixture(scope='function')
def check_box_form(page: Page) -> CheckBoxPage:
    return CheckBoxPage(page)