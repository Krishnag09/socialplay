
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options )
driver.get("https://creators.aiva.ai/login")
time.sleep(5)
driver.find_element_by_css_selector("#login-window > div.login-first-step > input").send_keys("kirillmasychev@outlook.com")
driver.find_element_by_css_selector("#button-container > div").click()
time.sleep(2)
driver.find_element_by_name("password").send_keys("dh_hacks2021")
driver.find_element_by_css_selector("#button-container").click()
time.sleep(2)
driver.find_element_by_css_selector("#crisp-chatbox > div > a > span.cc-1c9v > span > span > span > span.cc-tkyh > span > span.cc-g0ak.cc-hy0f").click()
create_button = driver.find_element_by_css_selector("#sidebar > div.menu.round-button.create-button")
time.sleep(2)
driver.execute_script("arguments[0].click();", create_button)
time.sleep(2)
musictype = driver.find_element_by_xpath("//*[contains(text(), 'Modern Cinematic')]") #enter string for the genre
time.sleep(2)
driver.execute_script("arguments[0].click();", musictype)
time.sleep(2)
driver.find_element_by_xpath("//*[contains(text(), 'Key Signature')]").click()
time.sleep(3)
driver.close()