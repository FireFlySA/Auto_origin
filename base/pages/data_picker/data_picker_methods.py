import allure

from base.pages.data_picker.data_picker_page import DataPickerPage
from settings import Settings
from src.config.expectations import Wait


class DataPickerMethods:

    @staticmethod
    def date_picker_fill(data_picker_form: DataPickerPage):
        errors = []
        Wait.set_page(data_picker_form.page)
        try:
            with allure.step("Ввод даты второго датапикера"):
                data_picker_form.date_and_time.click()
                Wait.visible(data_picker_form.Wait_date_and_time)
                data_picker_form.date_and_time_month.click()
                data_picker_form.date_and_time_month_m.click()
                data_picker_form.date_and_time_year.click()
                data_picker_form.date_and_time_year_y.click()
                data_picker_form.date_and_time_day.click()
                data_picker_form.date_and_time_time.hover()
                data_picker_form.page.mouse.wheel(0, 300);
                data_picker_form.date_and_time_time_min.click()

            with allure.step("Создание скриншота"):
                screenshot_path = Settings.get_screenshot_path(file_name='data_picker.png')
                data_picker_form.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот страницы')







        # with allure.step('Создание скриншота до отправки формы'):
            #     screenshot_path = Settings.get_screenshot_path(file_name='data_picker_form.png')
            #     data_picker_form.page.screenshot(path=screenshot_path)
            #     allure.attach.file(source=screenshot_path, name='Скриншот формы')
            # with allure.step("Подтверждение формы"):
            #     data_picker_form.submit.click()


        except AssertionError as e:
            errors.append(str(e))
