from selenium import webdriver
import time

chromedriver_location = "chromedriver.exe" #C:\Users\Kiril\Documents\DH_hackathon_2021\socialplay\chromedriver.exe

driver = webdriver.Chrome(chromedriver_location)
driver.get('https://creators.aiva.ai/')
time.sleep(2)


email_address = 'kirillmasychev@outlook.com'
password = 'dh_hacks2021'

email_input = '//*[@id="login-window"]/div[2]/input'
continue_button = '//*[@id="button-container"]/div'
password_input = '//*[@id="login-window"]/div[2]/input[2]'
sign_in_button = '//*[@id="button-container"]/div'


driver.find_element_by_xpath(email_input).send_keys(email_address)
driver.find_element_by_xpath(continue_button).click()
driver.find_element_by_xpath(password_input).send_keys(password)
driver.find_element_by_xpath(sign_in_button).click()