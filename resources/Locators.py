#!/usr/bin/env python3
from selenium.webdriver.common.by import By
'''
Locators File

Holds all Locations By Name and locator strategy.
'''

'''
usage of By import
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
example: By.CLASS_NAME, 'class-name'
Description:
File for all properly named locators for paths using proper linkage from above.
ex.
constant_name = `tuple`(By.`names_from_above`, quoted=needed name)
'''

class Locators():
    # --- Profile Page Locators ---
    #? chooses Mikey's profile from selection.
    CHOOSE_PROFILE = (By.XPATH, '//*[@id="appMountPoint"]/div/div/div[1]/div[1]/div[2]/div/div/ul/li[2]/div/a/div/div')
    