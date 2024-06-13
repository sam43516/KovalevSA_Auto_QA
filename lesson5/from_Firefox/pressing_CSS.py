from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# Откройте страницу http://uitestingplayground.com/classattr
driver = webdriver.Firefox()
driver.get('http://uitestingplayground.com/classattr')
driver.maximize_window()

# Кликните на синюю кнопку
clickable = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
clickable.click()
sleep(2)
driver.switch_to.alert.accept()
sleep(2)
driver.close()

#Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.
x = 0 
while x < 3:
    driver = webdriver.Firefox()
    driver.get('http://uitestingplayground.com/classattr')
    driver.maximize_window()
    clickable = driver.find_element(By.XPATH, "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    clickable.click()
    sleep(2)
    driver.switch_to.alert.accept()
    sleep(2)
    x+=1
    driver.close()

