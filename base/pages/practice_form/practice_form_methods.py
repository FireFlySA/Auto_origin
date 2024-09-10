from time import sleep
import allure

from base.pages.practice_form.practice_form_page import PracticeFormPage
from settings import Settings
from src.config.expectations import Wait


class PracticeFormMethods:

    @staticmethod
    def fill_name_input(practice_form: PracticeFormPage):
        errors = []
        Wait.set_page(practice_form.page)
        try:
            with allure.step("Ввод имени и фамилии"):
                practice_form.first_name.fill("Иван")
                practice_form.last_name.fill("Иванов")
            with allure.step("Ввод email"):
                practice_form.email.fill("test@test.com")
            with allure.step("Выбор гендера"):
                practice_form.gender.click()
            with allure.step("Ввод телефона"):
                practice_form.mobile.fill("88007654321")
            with allure.step("Ввод даты"):
                practice_form.data_picker.click()
                Wait.visible(practice_form.Wait_data_picker_months)
                practice_form.data_picker_months.select_option('May')
                practice_form.data_picker_year.select_option('1991')
                practice_form.data_picker_day.click()
                Wait.hidden(practice_form.Wait_data_picker_months)

            with allure.step("Ввод темы сообщения"):
                practice_form.subject.fill("Maths")
                practice_form.page.keyboard.down('Tab')
            with allure.step("Выбор хобби"):
                practice_form.hobbies.click()
            with allure.step('Загрузка файла'):
                practice_form.picture.load_file('media/sample-birch-400x300.jpg')
            with allure.step("Ввод адреса"):
                practice_form.current_address.fill("г. Краснодар, ул. Старокубанская 114")
            with allure.step("Выбор штата"):
                practice_form.state.click()
                practice_form.page.keyboard.down('Tab')
            with allure.step("Выбор города"):
                practice_form.city.click()
                practice_form.page.keyboard.down('Tab')
            with allure.step('Создание скриншота до отправки формы'):
                screenshot_path = Settings.get_screenshot_path(file_name='practice_form.png')
                practice_form.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот формы')
            with allure.step("Подтверждение формы"):
                practice_form.submit.click()
            with allure.step("Создание скриншота после отправки формы"):
                Wait.visible(practice_form.Wait_result)
                screenshot_path = Settings.get_screenshot_path(file_name='practice_form_modal.png')
                practice_form.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот модалки')

        except AssertionError as e:
            errors.append(str(e))
