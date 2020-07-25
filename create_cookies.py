#!/home/alexander/Programmierung/Python/web_dev_env/bin/python
import os
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def dump_cookies():
    dirname = os.path.dirname(__file__)
    cooky = os.path.join(dirname, 'cookies.json')   
    with open (cooky, 'w') as f:
        json.dump(driver.get_cookies(), f, indent=2)

options = FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
driver.get("https://udemy.com")

time.sleep(10)

dump_cookies()