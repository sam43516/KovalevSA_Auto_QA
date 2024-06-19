from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Откройте страницу https://the-internet.herokuapp.com/entry_ad
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/entry_ad')
driver.maximize_window()
sleep(2)

# В модальном окне нажмите на кнопку Сlose
modal_click = driver.find_element(By.XPATH, '//p[text()="Close"]')
modal_click.click()
sleep(2)
