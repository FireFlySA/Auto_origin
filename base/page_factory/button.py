import os
import time

import allure

from base.page_factory.component import Component
from settings import BASE_DIR


class Button(Component):
    @property
    def type_of(self) -> str:
        return 'кнопка'

    def hover(self, **kwargs) -> None:
        """
        Выполняет наведение курсора на кнопку.
        """
        with allure.step(f'Наведение курсора на {self.type_of} с именем "{self.name}"'):
            self.should_be_visible()
            locator = self.get_locator(**kwargs)
            locator.hover()

    def double_click(self, **kwargs):
        """
        Двойное нажатие на кнопку.
        """
        with allure.step(f'Двойное нажатие на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.dblclick()

    def on_click(self, **kwargs) -> None:
        """
        Нажатие на кнопку.
        """
        with allure.step(f'Нажатие на {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click()

    def check_class(self, name, **kwargs):
        """
        Проверка класса кнопки.
        """
        with allure.step(f'Проверка класса {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            time.sleep(2)
            classes = locator.get_attribute("class")
            ass = name in classes
            assert ass, f"{self.name} -> {ass}"

    def is_visible(self, last=False, **kwargs):
        """
        Проверка видимости кнопки.
        """
        with allure.step(f'Проверка видимости {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            return locator.is_visible()

    def right_click(self, **kwargs):
        """
        Нажатие на правую кнопку мыши.
        """
        with allure.step(f'Нажати правой кнопкой мыши {self.type_of} с именем "{self.name}"'):
            locator = self.get_locator(**kwargs)
            locator.click(button='right')

    def download_file(self, **kwargs):
        with allure.step(f'Скачивание файла из кнопки "{self.name}"'):
            with self.page.expect_download() as download_info:
                locator = self.get_locator(**kwargs)
                locator.click()
            download = download_info.value
            download.save_as(os.path.join(BASE_DIR, "src", "downloads", download.suggested_filename))