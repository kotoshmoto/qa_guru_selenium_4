import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with, with_tag_name


# Для работы относительных локаторов необходимо импортировать класс with_tag_name (или with_name / with_id)
# из модуля selenium.webdriver.support.relative_locator.

def test_relative_locator(driver):
    driver.get("https://qa-guru.github.io/one-page-form/text-box.html")

    # below
    text_box_label = driver.find_element(By.XPATH, "/html/body/main/section/h1")
    full_name_label = driver.find_element(locate_with(By.TAG_NAME, "input").below(text_box_label))
    full_name_label.clear()
    full_name_label.send_keys("Ivan Ivanov")

    # above
    curr_addr_locator = driver.find_element(By.ID, "currentAddress")
    email_input = driver.find_element(locate_with(By.TAG_NAME, "input").above(curr_addr_locator))
    email_input.clear()
    email_input.send_keys("ivan@example.com")

    # TODO: Fix me. Справа в форме Text Box нет элементов которые можно использовать
    # second_radio = driver.find_element(By.ID, "gender-radio-2")
    # first_radio = driver.find_element(locate_with(By.TAG_NAME, "input").to_left_of(second_radio))
    # first_radio.click()

    # to_right_of
    curr_addr_label = driver.find_element(By.XPATH, '//*[@id="userForm"]/div[3]/label')
    curr_addr_input = driver.find_element(locate_with(By.TAG_NAME, "textarea").to_right_of(curr_addr_label))
    curr_addr_input.clear()
    curr_addr_input.send_keys("г. Минск, ул. Академическая")

    perm_addr_label = driver.find_element(By.XPATH, '//*[@id="userForm"]/div[4]/label')
    perm_addr_input = driver.find_element(locate_with(By.TAG_NAME, "textarea").to_right_of(perm_addr_label))
    perm_addr_input.clear()
    perm_addr_input.send_keys("г. Минск, ул. Академическая")

    # near
    label_element = driver.find_element(By.ID, "permanentAddress")
    submit_button = driver.find_element(locate_with(By.TAG_NAME, "button").near(label_element))
    submit_button.click()
