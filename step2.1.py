from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/execute_script.html"
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
  
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)

    
    input4 = browser.find_element(By.ID, "answer")
    input4.send_keys(y)
    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()
    button2 = browser.find_element(By.ID, "robotsRule")

    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    button2.click()
    
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
