from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


# Откройте страницу http://the-internet.herokuapp.com/inputs
driver = webdriver.Firefox()
driver.get('http://the-internet.herokuapp.com/inputs')
driver.maximize_window()

# Введите в поле текст 1000
input_ = driver.find_element(By.CSS_SELECTOR, "[type='number']")
sleep(3)
input_.send_keys("1000")
sleep(3)

# Очистите это поле (метод clear)
input_.clear()
sleep(3)

# Введите в это же поле текст 999
input_.send_keys("999")
sleep(3)
driver.close()
