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
import time

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

db_path = os.path.join(ROOT_DIR, 'db.sqlite3')
sqlite_file = os.path.join(db_path)
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

FFdriver = ROOT_DIR + r"/geckodriver"
browser = webdriver.Firefox(executable_path=FFdriver)


browser.get("https://www.ebag.bg/")

def main():
	promoPage = browser.find_element_by_xpath("/html/body/header/div[3]/div/div/ul/li[1]/a")
	promoPage.click()

	pageLanguage = browser.find_element_by_xpath("/html/body/header/div[3]/div/div/ul/li[5]/a")

	if pageLanguage.text == "EN":
		pageLanguage.click()
	else:
		pass

	time.sleep(15)

	browser.quit()

	time.sleep(100)
	for i in range(1,100):
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(1)

main()
print("Hello World!")

























