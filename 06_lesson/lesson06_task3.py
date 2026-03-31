from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    wait = WebDriverWait(driver, 10)

    images = wait.until(lambda d: d.find_elements(
        By.CSS_SELECTOR, "#image-container img") if len(
            d.find_elements(
                By.CSS_SELECTOR, "#image-container img")) >= 3 else False)

    wait.until(lambda d: all(img.get_attribute("src") for img in images))

    third_image = images[2]

    src_value = third_image.get_attribute("src")

    print(src_value)

finally:
    driver.quit()
