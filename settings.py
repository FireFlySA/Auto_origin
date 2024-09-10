import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Settings:
    @property
    def base_url(self) -> str:
        """
        Возвращает основной URL для API.

        Этот URL используется для всех API-запросов в системе.
        Его можно легко изменить для использования с другим окружением.
        """
        return "https://demoqa.com"

    @staticmethod
    def get_screenshot_path(file_name: str) -> str:
        return os.path.join(BASE_DIR, "src", "screenshots", file_name)

    @staticmethod
    def get_media_path(file_name: str) -> str:
        return os.path.join(BASE_DIR, "media", file_name)

