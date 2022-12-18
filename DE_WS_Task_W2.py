#!/usr/bin/env python
# coding: utf-8

# In[4]:
# provide web driver folder path in webdr_loc in raw format i.e r'path'
# provide the url in the path parameter.
class DataDownloader2():
    
    def __init__(self, path, webdr_loc):
        self.webdr_loc = webdr_loc
        self.path = path

    def load_module(self):
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.common.action_chains import ActionChains
        import csv
        import pdb
        import pandas as pd
        import time
        import os.path

        # Headless mode
        options = Options()  # Initialize an instance of the Options class
        options.headless = True  # True -> Headless mode activated


        website = self.path
        path = self.webdr_loc
        driver = webdriver.Chrome(path,options=options)
        driver.get(website)
        # driver.maximize_window()

        elem = driver.find_element(By.XPATH, '//a[contains(@href, "event-search")]')
        new_path = elem.get_attribute("href")

        driver.quit()

        website = new_path
        path = self.webdr_loc
        driver = webdriver.Chrome(path)
        driver.get(website)
        driver.maximize_window()

        records = []

        button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//button[@aria-label = "Download"]')))
        driver.implicitly_wait(10)
        ActionChains(driver).move_to_element(button).click(button).perform()


        button2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[@id="downloadButton"]')))
        # pdb.set_trace()
        driver.implicitly_wait(10)

        ActionChains(driver).move_to_element(button2).click(button2).perform()
        # Implicit Wait
        time.sleep(10)

        driver.quit()







