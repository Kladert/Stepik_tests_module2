from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
link = "http://suninjuly.github.io/file_input.html"

try:
  
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("1")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("2")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("3@3")
    input4 = browser.find_element(By.NAME, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    input4.send_keys(file_path)
    
    button3 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button3.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
