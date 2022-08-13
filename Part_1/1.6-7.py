from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    fields = browser.find_elements(By.TAG_NAME, 'input')
    for row in fields:
        row.send_keys("twrchi-eto-pzdc")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()