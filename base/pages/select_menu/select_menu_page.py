from playwright.sync_api import Page

from base.page_factory.input import Input


class SelectMenuPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""

        self.select_value = Input(page, locator='//*[@id="withOptGroup"]', name='Выбор значения 1 селекта')
        self.select_one = Input(page, locator='//*[@id="selectOne"]', name='Выбор значения 2 селекта')
        self.select_old_style = Input(page, locator='//*[@id="oldSelectMenu"]', name='Выбор значения 3 селекта')
        self.multiselect = page.locator('(//*[@class=" css-2b097c-container"])[position()=3]')
        self.multiselect_option_0 = page.locator('//*[starts-with(@id, "react-select-")]').get_by_text('Green')
        self.multiselect_option_1 = page.locator('//*[starts-with(@id, "react-select-")]').get_by_text('Blue')
        self.multiselect_option_2 = page.locator('//*[starts-with(@id, "react-select-")]').get_by_text('Black')
        self.multiselect_option_3 = page.locator('//*[starts-with(@id, "react-select-")]').get_by_text('Red')
        self.standard_multiselect = page.locator('//*[@id="cars"]')

        """Ожидания"""

        self.Wait_multiselect = '(//*[@class=" css-2b097c-container"])[position()=3]'
