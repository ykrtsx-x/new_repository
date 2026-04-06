from selenium.webdriver.common.by import By


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    DELAY_INPUT = (By.ID, "delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")

    def button(self, value):
        return (By.XPATH, f"//span[text()='{value}']")

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        element = self.driver.find_element(*self.DELAY_INPUT)
        element.clear()
        element.send_keys(value)

    def click(self, value):
        self.driver.find_element(*self.button(value)).click()

    def get_result(self):
        return self.driver.find_element(*self.SCREEN).text
