import allure
from lesson_10.pages.login_page import LoginPage


@allure.title("Пустые поля логина")
@allure.description("Проверка ошибки при пустых данных")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.NORMAL)
def test_empty_login(driver):

    page = LoginPage(driver)

    with allure.step("Открыть страницу"):
        page.open("https://example.com/login")

    with allure.step("Нажать вход без данных"):
        page.click_login()

    with allure.step("Проверить ошибку"):
        assert page.get_error_message() != ""
