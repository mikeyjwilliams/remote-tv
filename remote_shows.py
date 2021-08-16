#!/usr/bin/env python3
import os
import platform
from env.env import Env 
from utility.Driver import Driver, WebDriver
from utility.Utility import Utility
from resources.Locators import Locators
from selenium import webdriver
import time

def browse():

    browser = WebDriver(Driver)
    driver = browser.main_webdriver('chrome')

    driver.('google.com')

    time.sleep(4)

    close_browser = WebDriver(Driver)
    close_browser.close_driver()

browse()