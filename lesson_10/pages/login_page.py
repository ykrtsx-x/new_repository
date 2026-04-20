from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:
    """
    Класс страницы авторизации.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        :param driver: экземпляр WebDriver
        """
        self.driver = driver

    def open(self, url: str) -> None:
        """
        Открывает страницу авторизации.

        :param url: URL страницы
        :return: None
        """
        self.driver.get(url)

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: логин пользователя
        :return: None
        """
        self.driver.find_element(By.ID, "username").send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: пароль пользователя
        :return: None
        """
        self.driver.find_element(By.ID, "password").send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку логина.

        :return: None
        """
        self.driver.find_element(By.ID, "login").click()

    def get_error_message(self) -> str:
        """
        Получает текст ошибки.

        :return: текст ошибки
        """
        return self.driver.find_element(By.ID, "error").text
