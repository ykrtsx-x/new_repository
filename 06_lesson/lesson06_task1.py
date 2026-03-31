from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")

    wait = WebDriverWait(driver, 10)

    button = driver.find_element(By.ID, "ajaxButton")
    button.click()

    success_text = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, ".bg-success"))
    )

    text = success_text.text

    print(text)

finally:
    driver.quit()
