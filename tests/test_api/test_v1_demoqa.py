import allure

from base.pages.api_pages.authorized.methods_v1_authorized import MethodsAuthorized


class TestAuthorizedV1Account:
    """
    Класс, содержащий тесты для проверки авторизации пользователя и генерации токена через API.

    Этот класс включает два теста:
    1. Тест на авторизацию пользователя.
    2. Тест на генерацию токена для авторизованного пользователя.
    3. Тест на создание пользователя

    Тесты выполняются с использованием Allure для документирования шагов и результатов.
    """

    @allure.epic('API')
    @allure.title('Авторизация v1')
    def test_authorized_v1_account(self):
        """
        Тест для проверки авторизации пользователя через POST-запрос на эндпоинт /Account/v1/Authorized.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_v1_account_authorized` из класса `MethodsAuthorized`, который:
           - Формирует данные для запроса.
           - Отправляет POST-запрос на сервер для авторизации пользователя.
           - Валидирует ответ сервера, проверяя успешность авторизации.

        Результаты теста записываются в отчет Allure, включая шаги формирования данных, отправки запроса и валидации ответа.
        Если тест проходит успешно, в консоль выводится информация о статусе авторизации. В случае ошибки тест завершится
        с сообщением об ошибке, которое будет включено в отчет Allure.
        """
        MethodsAuthorized.post_v1_account_authorized()

    @allure.epic('API')
    @allure.title('Генерация токена v1')
    def test_generate_token_v1(self):
        """
        Тест для проверки генерации токена пользователя через POST-запрос на эндпоинт /Account/v1/GenerateToken.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_token_authorized` из класса `MethodsAuthorized`, который:
           - Формирует данные для запроса.
           - Отправляет POST-запрос на сервер для генерации токена.
           - Валидирует ответ сервера, проверяя успешность генерации токена.

        Результаты теста записываются в отчет Allure, включая шаги формирования данных, отправки запроса и валидации ответа.
        Если тест проходит успешно, в консоль выводится информация о сгенерированном токене и статусе операции. В случае ошибки
        тест завершится с сообщением об ошибке, которое будет включено в отчет Allure.
        """
        MethodsAuthorized.post_token_authorized()

    @allure.epic('API')
    @allure.title('Создание юзера v1')
    def test_reg_user_v1(self):
        """
        Тест для регистрации пользователя через POST-запрос на эндпоинт /Account/v1/User.

        Этот тест выполняет следующие шаги:
        1. Вызывает метод `post_user_register` из класса `MethodsAuthorized`, который:
           - Формирует данные для запроса.
           - Отправляет POST-запрос на сервер для регистрации пользователя.
           - Валидирует ответ сервера, проверяя успешность создания.

        Результаты теста записываются в отчет Allure, включая шаги формирования данных, отправки запроса и валидации ответа.
        Если тест проходит успешно, в консоль выводится информация о сгенерированном токене и статусе операции. В случае ошибки
        тест завершится с сообщением об ошибке, которое будет включено в отчет Allure.
        """
        MethodsAuthorized.post_user_register()
