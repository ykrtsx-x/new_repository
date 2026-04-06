from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first, last, zip_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first)
        self.driver.find_element(*self.LAST_NAME).send_keys(last)
        self.driver.find_element(*self.ZIP).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE).click()

    def get_total(self):
        return self.driver.find_element(*self.TOTAL).text
