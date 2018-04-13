#!/usr/bin/env python

######################################################
#
# shopper - check for deals on your shopping preferences
# written by Petar Petkov (petkov.generali@gmail.com)
#
######################################################

import os
import sys
import sqlite3
import datetime

from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException

import win32com.client


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(ROOT_DIR, 'db.sqlite3')
sqlite_file = os.path.join(db_path)
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

prefs = {"download.default_directory" : ROOT_DIR}
FFdriver = ROOT_DIR + r"\firefoxdriver.exe"
profile = FirefoxProfile()

profile.set_preference("browser.download.folderList",2)
profile.set_preference("browser.download.manager.showWhenStarting",False)
profile.set_preference("browser.download.dir", ROOT_DIR)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', "text/plain, application/vnd.ms-excel, text/csv, application/csv, text/comma-separated-values, application/download, application/octet-stream, binary/octet-stream, application/binary, application/x-unknown")

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
binary2 = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)


try:
    browser = webdriver.Firefox(executable_path=FFdriver,firefox_profile=profile,firefox_binary=binary)
except:
    browser = webdriver.Firefox(executable_path=FFdriver,firefox_profile=profile,firefox_binary=binary2)


print("Hello World!")