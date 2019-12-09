import json
import datetime
import time
from selenium import webdriver

with open('config.json') as f:
    data = json.load(f)

website = 'https://dziekanat.agh.edu.pl/'
elective_module_suffix = 'WyborPrzedmiotowCC.aspx'


def login_user(driver):
    login_input = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtIdent')
    login_input.send_keys(data["login"])

    password_input = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtHaslo')
    password_input.send_keys(data["password"])

    login_button = driver.find_element_by_xpath("//input[@value='Zaloguj']")
    login_button.click()


def select_elective_modules(driver):
    select_buttons = driver.find_elements_by_xpath("//*[text()='Wybór']")
    select_buttons[1].click()

    for module in data["partial_module_names"]:
        elements = driver.find_elements_by_xpath(f"//input[contains(@value,'{module}')]")
        elements[1].click()

    move_left = driver.find_element_by_xpath("//input[@value='>>>']")
    move_left.click()

    next_button = driver.find_element_by_xpath("//input[@value='Dalej']")
    next_button.click()


def wait_until_active():
    current_time = datetime.datetime.today()
    hour, minute, second = [int(t) for t in data["time"].split(":")]
    target_time = datetime.datetime(current_time.year, current_time.month, current_time.day, hour, minute, second + 1)
    while datetime.datetime.today() < target_time:
        print(datetime.datetime.today())
        time.sleep(1)


def main():
    driver = webdriver.Firefox(executable_path='geckodriver')
    driver.get(website)
    login_user(driver)
    driver.get(website + elective_module_suffix)
    wait_until_active()
    select_elective_modules(driver)
    print(datetime.datetime.today())


if __name__ == '__main__':
    main()
