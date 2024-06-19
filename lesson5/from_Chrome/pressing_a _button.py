from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/
driver = webdriver.Chrome()
driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
driver.maximize_window()

# Пять раз кликните на кнопку Add Element
x = 0
while x < 5:
    clickable = driver.find_element(
        By.CSS_SELECTOR, '[onclick="addElement()"]'
        )
    ActionChains(driver).click(clickable).perform()
    x += 1

# Соберите со страницы список кнопок Delete
buttons = driver.find_elements(By.CSS_SELECTOR, '[class="added-manually"]')

# Выведите на экран размер списка
print("Размер списка = " + str(len(buttons)))
