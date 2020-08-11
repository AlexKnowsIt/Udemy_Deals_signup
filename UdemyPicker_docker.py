#!/home/alexander/Programmierung/Python/web_dev_env/bin/python
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

def read_Mydealz():
    web_input = '/MydealzInput/gistfile1.txt'
    with open(web_input) as f:
        links = f.readlines()
    return(links)

def add_cookies():
    cooky = '/cookies.json'
    with open(cooky, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        driver.add_cookie(cookie)

caps = DesiredCapabilities.FIREFOX
driver = webdriver.Remote(command_executor='http://172.18.0.2:4444', desired_capabilities=caps)

driver.get("https://udemy.com")

add_cookies()

links = read_Mydealz()

for link in links:
    driver.get(link)
    try:
        element = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".udlite-heading-xxl"))
        )
        prices = driver.find_elements_by_css_selector(".udlite-heading-xxl > span:nth-child(2)")
        for preis in prices:
            price = preis
        lang = driver.find_element_by_css_selector(".clp-lead__locale")
        if price.text == "Kostenlos" and (lang.text == "Englisch" or lang.text == "Deutsch"):
            btn = driver.find_element_by_css_selector(".sidebar-container--purchase-section--17KRp > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)")
            print(driver.title + " wurde deiner Kursliste hinzugefügt.")
            btn.click()
            time.sleep(5)
            try:
                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '.mb-space-sm'))
                )
                # print(driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/form/div[2]/div/div[1]/table[2]/tbody/tr/td[2]/span/span').text)
                # print(driver.find_element_by_xpath('.styles--checkout-pane-outer--1syWc > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)').text)
                if driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/form/div[2]/div/div[1]/table[2]/tbody/tr/td[2]/span/span').text=='0,00 €':
                    btn = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/div/div/div[2]/form/div[2]/div/div[4]/button")
                    btn.click()
                    time.sleep(3)
                else:
                    print('Preis nicht erkannt bei Bestätigungsseite')
            except:
                print('Kein Preis erschienen auf Bestätigungsseite')

        else:
            print("Kurs nicht mehr kostenlos")
    except:
        print("Kein Preiselement")
driver.close()