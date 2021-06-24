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