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

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities




ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

if platform == "linux":
	print("Linux")
	FFdriver = ROOT_DIR + r"/firefoxdriver"
elif platform == "darwin":
	print("Mac")
	FFdriver = ROOT_DIR + r"/firefoxdriver"
elif platform == "win32" or "cygwin":
	print("Windows")
	FFdriver = ROOT_DIR + r"/firefoxdriver"
else:
	print("Can't identify os")




db_path = os.path.join(ROOT_DIR, 'db.sqlite3')
sqlite_file = os.path.join(db_path)
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = False

prefs = {"download.default_directory" : ROOT_DIR}

profile = FirefoxProfile()
 
binary = FirefoxBinary('/Users/retina/Applications/Firefox.app', log_file=sys.stdout)

browser = webdriver.Firefox(capabilities=cap, executable_path=FFdriver,firefox_profile=profile,firefox_binary=binary)


browser.get("https://www.ebag.bg/")

def main():
	promoPage = browser.find_element_by_xpath("/html/body/header/div[3]/div/div/ul/li[1]/a")

	promoPage.click()

print("Hello World!")

























