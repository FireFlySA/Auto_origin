from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input
from src.config.expectations import Wait


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]', name='Почта')
        self.gender = Input(page, locator='//*[@for="gender-radio-2"]', name='Пол')
        self.mobile = Input(page, locator='//*[@id="userNumber"]', name='Телефон')

        """"Датапикер"""
        self.data_picker = page.locator('//*[@id="dateOfBirthInput"]')
        self.data_picker_months = page.locator('//*[@class="react-datepicker__month-select"]')
        self.data_picker_year = page.locator('//*[@class="react-datepicker__year-select"]')
        self.data_picker_day = page.locator('//*[starts-with(@class, "react-datepicker__day")]').get_by_text('19')

        self.subject = Input (page, locator='//*[@id="subjectsInput"]', name='тема')
        self.hobbies = Input (page, locator='//*[@for="hobbies-checkbox-2"]', name='хобби')
        self.picture = Input (page, locator='//*[@id="uploadPicture"]', name='картинка')
        self.current_address = Input(page, locator='//*[@id="currentAddress"]', name='адрес')
        self.state = Input(page, locator='//*[@id="state"]', name='Штат')
        self.city = Input(page, locator='//*[@id="city"]', name='город')
        self.submit = Button(page, locator='//*[@id="submit"]', name='Отправить')

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.Wait_email = '//*[@id="userEmail"]'
        self.Wait_gender = '//*[@id="gender-radio-2"]'
        self.Wait_mobile = '//*[@id="userNumber"]'
        self.Wait_data_picker_months = '//*[@id="dateOfBirthInput"]'
        self.Wait_subject = '//*[@id="subjectsInput"]'
        self.Wait_hobbies = '//*[@id="hobbies-checkbox-2"]'
        self.Wait_current_address = '//*[@id="currentAddress"]'
        self.Wait_state = '//*[@id="state"]'
        self.Wait_city = '//*[@id="city"]'
        self.Wait_submit = '//*[@id="submit"]'
        self.Wait_result = '//*[@class="modal-content"]'



