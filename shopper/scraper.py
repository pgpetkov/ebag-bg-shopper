#!/usr/bin/env python

######################################################
#
# shopper - check for deals based on your shopping history
# written by Petar Petkov (petkov.generali@gmail.com)
#
######################################################

import os
import sys
import sqlite3
import datetime
from sys import platform

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




ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if platform == "linux":
	print("Linux")
	FFdriver = ROOT_DIR + r"\firefoxdriver"
elif platform == "darwin":
	print("Mac")
	FFdriver = ROOT_DIR + r"\firefoxdriver"
elif platform == "win32" or "cygwin":
	print("Windows")
	FFdriver = ROOT_DIR + r"\firefoxdriver"
else:
	print("Can't identify os")




db_path = os.path.join(ROOT_DIR, 'db.sqlite3')
sqlite_file = os.path.join(db_path)
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

prefs = {"download.default_directory" : ROOT_DIR}

FFdriver = ROOT_DIR + r"\firefoxdriver.exe"
profile = FirefoxProfile()

binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)
binary2 = FirefoxBinary('C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe', log_file=sys.stdout)


try:
    browser = webdriver.Firefox(executable_path=FFdriver,firefox_profile=profile,firefox_binary=binary)
except:
    browser = webdriver.Firefox(executable_path=FFdriver,firefox_profile=profile,firefox_binary=binary2)







print("Hello World!")

























