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
    # --- Netflix Profile Page Locators ---
    #? chooses profile by name given.
    NETFLIX_CHOOSE_PROFILE = (By.CLASS_NAME, 'profile-name')
    # --- Netflix Search Page Locators ---
    #? Search tab button
    NETFLIX_SEARCH_BUTTON = (By.CLASS_NAME, 'searchTab')
    NETFLIX_SEARCH_INPUT = (By.CLASS_NAME, 'searchInput')
    