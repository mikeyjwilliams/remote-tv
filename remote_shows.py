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
    NETFLIX_BASE_URL = 'www.netflix.com'

# chrome build
chrome_options = Options()

chrome_options.add_argument('start-maximized')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument("--auto-open-devtools-for-tabs")

os_system = platform.system()
chrome_path = None
if os_system in 'Linux':
    chrome_path = '~/drivers/chromedriver'
else:
    chrome_path = '../drivers/chromedriver.exe'
    

driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

driver.get('https://www.netflix.com/login')

# email user login
email_login = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
# env user name send input
email_login.send_keys(Env.NETFLIX_USER)
# password login find path
password_login = driver.find_element_by_xpath('//*[@id="id_password"]')
# env password send input
password_login.send_keys(Env.NETFLIX_PASS)
# locate login button
login_button = driver.find_element_by_xpath('//*[@id="appMountPoint"]/div/div[3]/div/div/div[1]/form/button')
# click login button
login_button.send_keys(Keys.ENTER)

# locate all profiles available
profile_links = WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'profile-name')))
# second profile selected
second_profile = profile_links[1]
# choose second profile to select.
second_profile.click()

icon_search = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME,'icon-search')))
icon_search.click()


# search_input = WebDriverWait(driver, 20).until()
# search_input.send_keys('Hilda')
# search_input.send_keys(Keys.ENTER)






time.sleep(10)

driver.quit()






