from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_slow_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 60)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        delay = wait.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, "#delay")))
        delay.clear()
        delay.send_keys("45")

        driver.find_element(By.XPATH, "//span[text()='7']").click()
        driver.find_element(By.XPATH, "//span[text()='+']").click()
        driver.find_element(By.XPATH, "//span[text()='8']").click()
        driver.find_element(By.XPATH, "//span[text()='=']").click()

        wait.until(lambda d: d.find_element(
            By.CLASS_NAME, "screen").text == "15")

        result_text = driver.find_element(By.CLASS_NAME, "screen").text
        assert result_text == "15"

    finally:
        driver.quit()
