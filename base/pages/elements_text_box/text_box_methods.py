import allure

from base.pages.elements_text_box.text_box_page import TextBoxPage
from settings import Settings


class TextBoxMethods:

    @staticmethod
    def fill_name_input(elements_text_box:TextBoxPage):
        errors = []
        try:
            with allure.step("Ввод имени"):
                elements_text_box.full_name.fill("Иванова Мария Ивановна")
            with allure.step("Ввод email"):
                elements_text_box.email.fill("test@test.com")
            with allure.step("Ввод текущего адреса"):
                elements_text_box.current_address.fill("Москва, ул. Большая Садовая, д.112")
            with allure.step("Ввод постоянного адреса"):
                elements_text_box.permanent_address.fill("Ярославль, ул. Красная, д. 100")
            with allure.step("Подтверждение отправки формы"):
                elements_text_box.submit.click()
            with allure.step("Создание скриншота"):
                screenshot_path = Settings.get_screenshot_path(file_name='text_form.png')
                elements_text_box.page.screenshot(path=screenshot_path)
                allure.attach.file(source=screenshot_path, name='Скриншот успеха')

        except AssertionError as e:
            errors.append(str(e))