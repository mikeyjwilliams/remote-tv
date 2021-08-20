#!/usr/bin/env python3
from selenium import webdriver # allow launching browser
from selenium.webdriver.common.by import By # allow search with parameters
from selenium.webdriver.support.ui import WebDriverWait # allow waiting for page to load
from selenium.webdriver.support import expected_conditions as EC # determine whether the web page has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.options import Options # chrome options import
from selenium import webdriver # firefox options import
import platform # used for check using windows or linux
from time import sleep # for timeouts


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
        os_platform = platform.system() 
        if browser == 'chrome':
            chrome_options = Options()
            chrome_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
            
            chromedriver_path = None
            if os_platform == 'Linux':
                #! alter for your path to linux chrome driver
                chromedriver_path = '~/drivers/chromedriver'
            elif os_platform == 'Windows': #! alter for windows chrome driver executable.
                chromedriver_path = '../drivers/chromedriver.exe'
            else:
                print('no system')
                
            print('Chromedriver print ', chromedriver_path)  
            # chrome_option.add_argument(' - incognito')
            chrome_options.add_argument(chrome_user_agent)
            
            
            driver = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=chrome_options)
            driver.maximize_window()
            return driver
            
        if browser == 'mozilla':
            mozilla_options = webdriver.FirefoxOptions()
            mozilla_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'
            
            mozilladriver_path = None
            if os_platform in 'Linux':
                #! change to path needed for you. 
                mozilladriver_path = '~/drivers/geckodriver'
            else: #! change to path needed for you. Windows firefox executable.
                mozilladriver_path = '../drivers/geckodriver.exe'
            # if mozilla add to driver_option mozilla options
            mozilla_options.add_argument(mozilla_user_agent)
            

            driver = webdriver.Firefox(executable_path=mozilladriver_path, firefox_options=mozilla_options)
            driver.maximize_window()
            return driver
            
    
    def close_driver(self):
        '''
        close_driver
        
        end the {main_webdriver}
        quit entire browser 
        '''
        webdriver.Chrome.close()
        webdriver.Firefox.close()
        webdriver.Chrome.quit()
        webdriver.Firefox.quit()