from playwright.sync_api import Page

class DataPickerPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Дата пикер1"""

        self.select_date = page.locator('//*[@id="datePickerMonthYearInput"]')
        self.select_date_months = page.locator('//*[@class="react-datepicker__month-select"]')
        self.select_date_year = page.locator('//*[@class="react-datepicker__year-select"]')
        self.select_date_day = page.locator('//*[starts-with(@class, "react-datepicker__day")]').get_by_text('15')

        """Локаторы страницы: Дата пикер2"""

        self.date_and_time = page.locator('//*[@id="dateAndTimePickerInput"]')
        self.date_and_time_month = page.locator('//*[@class="react-datepicker__month-read-view"]')
        self.date_and_time_month_m = page.locator('//*[starts-with(@class, "react-datepicker__month-option")]').get_by_text('July')
        self.date_and_time_year = page.locator('//*[@class="react-datepicker__year-read-view"]')
        self.date_and_time_year_y = page.locator('//*[starts-with(@class, "react-datepicker__year-option")]').get_by_text('2023')
        self.date_and_time_day = page.locator('//*[starts-with(@class, "react-datepicker__day")]').get_by_text('13')
        self.date_and_time_time = page.locator('//*[@class="react-datepicker__time-list"]')
        self.date_and_time_time_min = page.locator('//*[starts-with(@class, "react-datepicker__time-list-item")]').get_by_text('23:00')



        """Ожидания"""

        self.Wait_select_date_months = '//*[@id="datePickerMonthYearInput"]'
        self.Wait_date_and_time = '//*[@class="react-datepicker"]'



