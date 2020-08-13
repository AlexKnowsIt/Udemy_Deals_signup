#!/home/alexander/Programmierung/Python/web_dev_env/bin/python
import os
import time
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json

class Udemy():
    dirname = os.path.dirname(__file__)
    def __init__(self, variation='n'):
        if variation == 'h':
            options = FirefoxOptions()
            options.add_argument("--headless")
            self.driver = webdriver.Firefox(options=options)
        elif variation == 'd':
            caps = DesiredCapabilities.FIREFOX
            self.driver = webdriver.Remote(command_executor='//firefox:4444', desired_capabilities=caps)
        elif variation == 'n':
            self.driver = webdriver.Firefox()
        else:
            raise NotImplementedError
        web_input = os.path.join(self.dirname, 'MydealzInput/gistfile1.txt')
        with open(web_input) as f:
            self.links = f.readlines()
        cooky = os.path.join(self.dirname, 'cookies.json')
        self.driver.get("https://udemy.com")
        with open(cooky, 'r') as f:
            cookies = json.load(f)
        for cookie in cookies:
            self.driver.add_cookie(cookie)
    
    def sign_up(self):
        for link in self.links:
            self.driver.get(link)
            try:
                element = WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".udlite-heading-xxl"))
                )
                prices = self.driver.find_elements_by_css_selector(".udlite-heading-xxl > span:nth-child(2)")
                for preis in prices:
                    price = preis
                lang = self.driver.find_element_by_css_selector(".clp-lead__locale")
                if price.text == "Kostenlos" and (lang.text == "Englisch" or lang.text == "Deutsch"):
                    btn = self.driver.find_element_by_css_selector(".sidebar-container--purchase-section--17KRp > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > div:nth-child(1) > button:nth-child(1)")
                    print(self.driver.title + " wurde deiner Kursliste hinzugefügt.")
                    btn.click()
                    time.sleep(5)
                    try:
                        element = WebDriverWait(self.driver, 3).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '.mb-space-sm'))
                        )
                        # print(self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div[2]/form/div[2]/div/div[1]/table[2]/tbody/tr/td[2]/span/span').text)
                        # print(self.driver.find_element_by_xpath('.styles--checkout-pane-outer--1syWc > div:nth-child(1) > div:nth-child(1) > table:nth-child(3) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > span:nth-child(1) > span:nth-child(1)').text)
                        try:
                            if self.driver.find_element_by_css_selector('.mb-space-sm').text=='Der Inhalt des Einkaufswagens ist kostenlos!':
                                btn = self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button")
                                btn.click()
                                time.sleep(3)
                            else:
                                print('Preis nicht erkannt bei Bestätigungsseite')
                        except:
                            print('Fehler auf Bestätigungsseite')
                    except:
                        print('Keine Bestätigungsseite')

                else:
                    print("Kurs nicht mehr kostenlos")
            except:
                print("Kein Preiselement")
        self.driver.close()