#!/usr/bin/env python3
import os
import platform
from env.env import Env 
from utility.Driver import WebDriver
from utility.Utility import Utility
from resources.Locators import Locators
from selenium import webdriver

def browse(self):

    browser = WebDriver()
    driver = browser.main_webdriver('chrome')

    driver.get('google.com')

    driver.wait(10)

    driver.close()

