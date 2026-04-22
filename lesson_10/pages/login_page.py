from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """
    Страница авторизации
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        :param driver: экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url: str) -> None:
        """
        Открывает страницу

        :param url: ссылка
        :return: None
        """
        self.driver.get(url)

    def enter_username(self, username: str) -> None:
        """
        Вводит логин

        :param username: логин пользователя
        :return: None
        """
        field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль

        :param password: пароль
        :return: None
        """
        field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        field.send_keys(password)

    def click_login(self) -> None:
        """
        Нажимает кнопку входа

        :return: None
        """
        button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button"))
        )
        button.click()

    def get_error_message(self) -> str:
        """
        Получает текст ошибки

        :return: текст ошибки
        """
        error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".error"))
        )
        return error.text
