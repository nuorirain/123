# задание 1
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def check_elements():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    time.sleep(2)

    username = driver.find_elements(By.ID, "user-name")
    password = driver.find_elements(By.ID, "password")
    login_button = driver.find_elements(By.ID, "login-button")

    if username and password and login_button:
        print("Элементы найдены")
    else:
        print("Элементы не найдены")

    driver.quit()

check_elements()
