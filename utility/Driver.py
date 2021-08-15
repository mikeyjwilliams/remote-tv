#!/usr/bin/env python3
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
import platform # used for check using windows or linux
import pytest # testing 
import time # for timeouts



class Driver():
    def __init__(self, driver):
        self.driver = driver
        

class WebDriver(Driver):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    
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
            # chrome_option = ChromeOptions()
            chrome_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            os_platform = platform.system()
            chromedriver_path = None
            if os_platform in 'Linux':
                chromedriver_path = '~/drivers/chromedriver'
            else:
                chromedriver_path = '../drivers/chromedriver.exe'
                
                
            # chrome_option.add_argument(' - incognito')
            self.driver.chrome_option.add_argument(chrome_user_agent)
            self.driver.chrome_option.add_argument('window-size=1200x600')
            
            return self.driver.Chrome(executable_path=chromedriver_path, chrome_options=self.driver.chrome_option)
            
        if browser == 'mozilla':
            mozilla_option = self.driver.FirefoxOptions()
            mozilla_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
            os_platform = 'Linux'
            if os_platform in 'Linux':
                mozilladriver_path = '~/drivers/geckodriver'
            else:
                mozilladriver_path = '../../../drivers/geckodriver.exe'
            # if mozilla add to driver_option mozilla options
            self.driver.mozilla_option.add_argument(mozilla_user_agent)
            mozilla_option.add_argument('window-size=1200x600')

            return self.driver.Firefox(executable_path=mozilladriver_path, firefox_options=mozilla_option)
            
    
    def close_driver(self):
        '''
        close_driver
        
        end the {main_webdriver}
        quit entire browser 
        '''
        self.driver.close()
        self.driver.quit()