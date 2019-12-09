import json
from selenium import webdriver

with open('data.json') as f:
    data = json.load(f)

driver = webdriver.Firefox(executable_path='geckodriver')
driver.get('https://dziekanat.agh.edu.pl/')
login_input = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtIdent')
login_input.send_keys(data["login"])

password_input = driver.find_element_by_id('ctl00_ctl00_ContentPlaceHolder_MiddleContentPlaceHolder_txtHaslo')
password_input.send_keys(data["password"])

login_button = driver.find_element_by_xpath("//input[@value='Zaloguj']")
login_button.click()

driver.get("https://dziekanat.agh.edu.pl/WyborPrzedmiotowCC.aspx")

select_buttons = driver.find_elements_by_xpath("//*[text()='Wybór']")
select_buttons[1].click()

for subject in data["partial_subject_names"]:
    elements = driver.find_elements_by_xpath(f"//input[contains(@value,'{subject}')]")
    for element in elements:
        element.click()

move_left = driver.find_element_by_xpath("//input[@value='>>>']")
move_left.click()

next_button = driver.find_element_by_xpath("//input[@value='Dalej']")
next_button.click()
