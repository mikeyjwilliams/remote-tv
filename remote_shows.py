#!/usr/bin/env python3
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.options import Options # chrome options import
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import platform # used for check using windows or linux
import time # time import

from env.env import Env

class TestData():
    NETFLIX_BASE_URL = 'www.netflix.com'

# chrome build
chrome_options = Options()

chrome_options.add_argument('start-maximized')


chrome_path = '../drivers/chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get('https://www.netflix.com/login')

email_login = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
email_login.send_keys(Env.NETFLIX_USER)
password_login = driver.find_element_by_xpath('//*[@id="id_password"]')
password_login.send_keys(Env.NETFLIX_PASS)
login_button = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
login_button.send_keys(Keys.ENTER)




time.sleep(5)





