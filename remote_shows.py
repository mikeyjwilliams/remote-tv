#!/usr/bin/env python3
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.options import Options # chrome options import
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import platform # used for check using windows or linux
import time # time import

from env.env import Env

class TestData():
    PEACOCK_SITE_LOGIN = 'https://peacocktv.com/signin'

# chrome build
chrome_options = Options()

chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-notifications')


os_system = platform.system()
chrome_path = None
if os_system in 'Linux':
    chrome_path = '~/drivers/chromedriver'
else:
    chrome_path = '../drivers/chromedriver.exe'

firefox_path = '../drivers/geckodriver.exe'  
    
driver = webdriver.Firefox(firefox_path=firefox_path, options=chrome_options)
# driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get(TestData.PEACOCK_SITE_LOGIN)

email_login = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.NAME, 'userIdentifier')))
email_login.send_keys(Env.PEACOCK_USER)

password_login = WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.ID, 'password')))
password_login.send_keys(Env.PEACOCK_PASSWORD)

submit_button = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'sign-in-form__submit')))
submit_button.click()




















