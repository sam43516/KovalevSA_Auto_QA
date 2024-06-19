from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


# Откройте страницу http://uitestingplayground.com/dynamicid.
driver = webdriver.Firefox()
driver.get('http://uitestingplayground.com/dynamicid')
driver.maximize_window()

# Кликните на синюю кнопку
clickable = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
ActionChains(driver).click(clickable).perform()
driver.close()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
x = 0
while x < 3:
    driver = webdriver.Firefox()
    driver.get('http://uitestingplayground.com/dynamicid')
    driver.maximize_window()
    clickable = driver.find_element(
        By.CSS_SELECTOR, '[class="btn btn-primary"]'
        )
    ActionChains(driver).click(clickable).perform()
    x += 1
    driver.close()
