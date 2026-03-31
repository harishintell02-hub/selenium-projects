from selenium import webdriver
from selenium.webdriver.common.by import By
from config.config import *
from project1_login.config.loc1.loc1 import *


driver = webdriver.Chrome()
driver.get(LOGIN_URL)
driver.maximize_window()


home_page_title = driver.find_element(By.XPATH,title_homepage)
home_page_title.is_displayed()

user_name_input_field = driver.find_element(By.ID,"username")
user_name_input_field.send_keys(USER_NAME_INPUT)


user_pwd_input_field = driver.find_element(By.ID,"password")
user_pwd_input_field.send_keys(USER_PWD_INPUT)

button_submit = driver.find_element(By.XPATH,submit_button)
button_submit.click()

success_mesg = driver.find_element(By.ID,'flash').text
print(success_mesg)
assert "You logged into a secure area!" in success_mesg

driver.quit()