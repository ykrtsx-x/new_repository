import allure
from lesson_10.pages.login_page import LoginPage


@allure.title("Неверный логин")
@allure.description("Проверка ошибки при неверных данных")
@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
def test_invalid_login(driver):

    page = LoginPage(driver)

    with allure.step("Открыть страницу"):
        page.open("https://the-internet.herokuapp.com/login")

    with allure.step("Ввести логин"):
        page.enter_username("wrong_user")

    with allure.step("Ввести пароль"):
        page.enter_password("wrong_pass")

    with allure.step("Нажать вход"):
        page.click_login()

    with allure.step("Проверить ошибку"):
        assert page.get_error_message() != ""
