from playwright.sync_api import Page

from base.page_factory.button import Button


class CheckBoxPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Чек-бокс"""
        self.first_button = Button(page, locator='(//*[@title="Toggle"])[position()=1]', name='1 уровень')
        self.second_button = Button(page, locator='(//*[@title="Toggle"])[position()=2]', name='2-1 уровень')
        self.third_button = Button(page, locator='(//*[@title="Toggle"])[position()=3]', name='2-2 уровень')
        self.fourth_button = Button(page, locator='(//*[@title="Toggle"])[position()=6]', name='2-3 уровень')
        self.fifth_button = Button(page, locator='(//*[@title="Toggle"])[position()=4]', name='3-1 уровень')
        self.sixth_button = Button(page, locator='(//*[@title="Toggle"])[position()=5]', name='3-1 уровень')
        self.angular_button = Button(page, locator='//*[@for="tree-node-angular"]', name='Кнопка Angular')
        self.private_button = Button(page, locator='//*[@for="tree-node-private"]', name='Кнопка Private')
        self.word_file_button = Button(page, locator='//*[@for="tree-node-wordFile"]', name='Кнопка WordFile')
        self.commands_button = Button(page, locator='//*[@for="tree-node-commands"]', name='Кнопка Commands')
        self.collapse_all_button = Button(page, locator='//*[@title="Collapse all"]', name='Кнопка свернуть все')


