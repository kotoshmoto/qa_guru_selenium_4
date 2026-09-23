import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


def test_drag_and_drop(driver):
    # Открытие тестового сайта
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    # Находим элементы для перемещения
    source_element = driver.find_element(By.ID, "column-a")
    target_element = driver.find_element(By.ID, "column-b")

    # Создаем цепочку действий для Drag and Drop
    actions = ActionChains(driver)

    # Зажимаем элемент A, переносим на B и отпускаем
    actions.drag_and_drop(source_element, target_element).perform()

    # Задержка для наглядности
    time.sleep(3)
