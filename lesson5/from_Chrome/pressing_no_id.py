from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton


# Откройте страницу http://uitestingplayground.com/dynamicid.

driver = webdriver.Chrome()
driver.get('http://uitestingplayground.com/dynamicid')
driver.maximize_window()

# Кликните на синюю кнопку
clickable = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
ActionChains(driver).click(clickable).perform()

# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
x = 0
while x < 3:
    driver = webdriver.Chrome()
    driver.get('http://uitestingplayground.com/dynamicid')
    driver.maximize_window()
    clickable = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    ActionChains(driver).click(clickable).perform()
    x+=1