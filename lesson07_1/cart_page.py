from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    CHECKOUT = (By.ID, "checkout")

    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT).click()

    def get_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
