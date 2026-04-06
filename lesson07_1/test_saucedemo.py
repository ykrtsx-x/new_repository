import sys
import os

sys.path.append(os.path.dirname(__file__))

from selenium import webdriver
from login_page import LoginPage
from inventory_page import InventoryPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_saucedemo():
    driver = webdriver.Firefox()

    try:
        login = LoginPage(driver)
        inventory = InventoryPage(driver)
        cart = CartPage(driver)
        checkout = CheckoutPage(driver)

        login.open()
        login.login("standard_user", "secret_sauce")

        inventory.add_item("Sauce Labs Backpack")
        inventory.add_item("Sauce Labs Bolt T-Shirt")
        inventory.add_item("Sauce Labs Onesie")

        inventory.go_to_cart()
        cart.click_checkout()

        checkout.fill_form("Ivan", "Ivanov", "12345")

        total = checkout.get_total()

        assert total == "Total: $58.29"

    finally:
        driver.quit()
