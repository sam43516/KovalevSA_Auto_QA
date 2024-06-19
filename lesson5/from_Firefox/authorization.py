from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Откройте страницу http://the-internet.herokuapp.com/login
driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/login')
driver.maximize_window()

# В поле username введите значение tomsmith
input_ = driver.find_element(By.CSS_SELECTOR, "#username")
sleep(2)
input_.send_keys("tomsmith")
sleep(2)

# В поле password введите значение SuperSecretPassword!
input_ = driver.find_element(By.CSS_SELECTOR, "#password")
sleep(2)
input_.send_keys("SuperSecretPassword!")
sleep(2)

# Нажмите кнопку Login
modal_click = driver.find_element(
    By.CSS_SELECTOR, '[class="fa fa-2x fa-sign-in"]'
    )
modal_click.click()
sleep(2)
driver.close()
