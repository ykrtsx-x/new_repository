import time
from selenium import webdriver
from calculator_page import CalculatorPage


def test_slow_calculator():
    driver = webdriver.Chrome()

    page = CalculatorPage(driver)

    page.open()
    page.set_delay("45")

    page.click("7")
    page.click("+")
    page.click("8")
    page.click("=")

    time.sleep(46)

    assert page.get_result() == "15"

    driver.quit()
