#!/usr/bin/env python3
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
import pytest # testing 
import time # for timeouts



class Driver():
    def __init__(self, driver):
        self.driver = driver
        
        
    
    def main_webdriver(self, browser: str):
        '''
        main_webdriver
        
        args: browser: str
        
        return webdriver.{browser} = chrome || firefox
        
        browser: str decides which webdriver is used
        FIXME: as of now set up only for windows.
        TODO: set up if statement for linux else windows path for chrome driver.
        '''
            
        if browser == 'chrome':
            chrome_option = self.driver.ChromeOptions()
            chrome_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            chromedriver_path = '../../../drivers/chromedriver.exe'
            # if chrome add to driver_option chrome options
            # chrome_option.add_argument(' - incognito')
            chrome_option.add_argument(chrome_user_agent)
            chrome_option.add_argument('window-size=1200x600')
            
            return self.driver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_option)
                
        if browser == 'mozilla':
            mozilla_option = webdriver.FirefoxOptions()
            mozilla_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
            mozilladriver_path = '../../../drivers/geckodriver.exe'
            # if mozilla add to driver_option mozilla options
            mozilla_option.add_argument(mozilla_user_agent)
            mozilla_option.add_argument('window-size=1200x600')

            return self.driver.Firefox(executable_path=mozilladriver_path, firefox_options=mozilla_option)
        
    
    def close_driver(self):
        '''
        close_driver
        
        end the {main_webdriver} 
        '''
        self.driver.close() 