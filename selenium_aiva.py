from selenium import webdriver
import time

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chromedriver_location = "chromedriver.exe"

driver = webdriver.Chrome(chromedriver_location)
def set_up():
    driver.get('https://creators.aiva.ai/')
    time.sleep(10)

action = ActionChains(driver)



email_address = 'kirillmasychev@outlook.com'
password = 'dh_hacks2021'

def login():
    # logs into aiva
    email_input = '//*[@id="login-window"]/div[2]/input'
    continue_button = '//*[@id="button-container"]/div'
    password_input = '//*[@id="login-window"]/div[2]/input[2]'
    sign_in_button = '//*[@id="button-container"]/div'


    driver.find_element_by_xpath(email_input).send_keys(email_address)
    driver.find_element_by_xpath(continue_button).click()
    driver.find_element_by_xpath(password_input).send_keys(password)
    driver.find_element_by_xpath(sign_in_button).click()


def create_new_song(input_genre, key_signature):
    # click create track button
    create_track_button = '//*[@id="sidebar"]/div[1]'
    driver.find_element_by_xpath(create_track_button).click()

    #selections to pick from
    genres = {
        'electronic': '//*[@id="preset-list"]/div[10]/div[1]',
        'hiphop': '//*[@id="preset-list"]/div[12]/div',
        'rock': '//*[@id="preset-list"]/div[7]/div[1]',
        'pop': '//*[@id="preset-list"]/div[6]/div[1]',
        #'ambient': '//*[@id="preset-list"]/div[11]/div[1]',
        'jazz': '//*[@id="preset-list"]/div[4]/div[1]'}

    # clicks on the specific genre
    driver.find_element_by_xpath(genres[input_genre]).click()
    time.sleep(3)
    if input_genre == "rock":
        rock("F# minor")

    if input_genre == "electronic":
        electronic(key_signature)
    if input_genre == "hiphop":
        hiphop(key_signature)
    if input_genre == "pop":
        pop(key_signature)
    if input_genre == "jazz":
        jazz(key_signature)

    time.sleep(3)

    create_your_track_button = "//*[contains(text(), 'Create your track(s)')]"
    driver.find_element_by_xpath(create_your_track_button).click()

    time.sleep(45)


def rock(key_signature):

    time.sleep(3)
    duration_button = "//*[contains(text(), 'Duration')]"


    driver.find_element_by_xpath(duration_button).click()
    action.move_to_element(driver.find_element_by_xpath(duration_button)).click()

    #to click on the individual options for duration button
    two_min_duration = '//*[@id="preset-parameters"]/div[4]/div/div[2]/div[6]'
    one_min_duration = '//*[@id="preset-parameters"]/div[4]/div/div[2]/div[4]'


    # because its a disappearing element, click on it when it is available
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH, one_min_duration))).click()
    time.sleep(2)

    select_key_signature(key_signature)

def electronic(key_signature):
    time.sleep(3)
    duration_button = '//*[@id="preset-parameters"]/div[3]/div/div[1]'

    driver.find_element_by_xpath(duration_button).click()
    action.move_to_element(driver.find_element_by_xpath(duration_button)).click()

    one_min_duration = '//*[@id="preset-parameters"]/div[3]/div/div[2]/div[5]'


    # because its a disappearing element, click on it when it is available
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, one_min_duration))).click()
    time.sleep(2)

    select_key_signature(key_signature)

def hiphop(key_signature):
    time.sleep(3)
    duration_button = '//*[@id="preset-parameters"]/div[3]/div/div[1]'

    driver.find_element_by_xpath(duration_button).click()
    action.move_to_element(driver.find_element_by_xpath(duration_button)).click()

    one_min_duration = '//*[@id="preset-parameters"]/div[3]/div/div[2]/div[5]'



    # because its a disappearing element, click on it when it is available
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, one_min_duration))).click()
    time.sleep(2)

    select_key_signature(key_signature)

def pop(key_signature):
    time.sleep(3)
    duration_button = '//*[@id="preset-parameters"]/div[4]/div/div[1]'

    driver.find_element_by_xpath(duration_button).click()
    action.move_to_element(driver.find_element_by_xpath(duration_button)).click()

    one_min_duration = '//*[@id="preset-parameters"]/div[4]/div/div[2]/div[4]'



    # because its a disappearing element, click on it when it is available
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, one_min_duration))).click()
    time.sleep(2)

    select_key_signature(key_signature)

def jazz(key_signature):
    time.sleep(3)
    duration_button = '//*[@id="preset-parameters"]/div[4]/div/div[1]'

    driver.find_element_by_xpath(duration_button).click()
    action.move_to_element(driver.find_element_by_xpath(duration_button)).click()

    one_min_duration = '//*[@id="preset-parameters"]/div[4]/div/div[2]/div[4]'


    # because its a disappearing element, click on it when it is available
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, one_min_duration))).click()
    time.sleep(2)

    select_key_signature(key_signature)


def select_key_signature(key_signature):
    # key signature
    key_signature_button = '//*[@id="preset-parameters"]/div[1]/div/div[2]'
    driver.find_element_by_xpath(key_signature_button).click()
    action.move_to_element(driver.find_element_by_xpath(key_signature_button)).click()

    any_major = '//*[@id="preset-parameters"]/div[1]/div/div[2]/div[2]'
    any_minor = '//*[@id="preset-parameters"]/div[1]/div/div[2]/div[3]'

    c_major = "//*[contains(text(), 'C major')]"
    f_major = '//*[@id="preset-parameters"]/div[1]/div/div[2]/div[5]'
    asharp_minor = "//*[contains(text(), 'A# minor')]"

    time.sleep(2)

    key_sig_xpath = f"//*[contains(text(), '{key_signature}')]"

    scroll = driver.find_element_by_xpath(key_sig_xpath)
    scroll.location_once_scrolled_into_view

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, key_sig_xpath))).click()


def press_play():

    num_of_tracks = 1

    for x in range(1,300):
        try:
            driver.find_element_by_xpath(f'//*[@id="track-view-list"]/div[1]/div/div[{x}]/div/div[2]')
        except:
            num_of_tracks = x-1
            break


    track_icon = f'//*[@id="track-view-list"]/div[1]/div/div[{num_of_tracks}]/div/div[2]'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, track_icon))).click()

    play_icon = f'//*[@id="track-view-list"]/div[1]/div/div[{num_of_tracks}]/div/div[2]'
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, play_icon))).click()



#login()
#time.sleep(3)
#create_new_song('rock')
#press_play()



