import re
import os
from bs4 import BeautifulSoup as BS
from selenium import webdriver as WD
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as WW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# website url
base_url = "https://anifume.com/33087/"
videos_url = "https://anifume.com/33087/Naruto-Shippuden-1-15"

# Chrome session
driver = WD.Chrome(executable_path=r"./chromedriver")
try:
    driver.get(videos_url)
    # WW(driver, 10).until(lambda x: x.find_elements_by_class_name("vplf")
    WW(driver, 10).until(lambda x: x.find_element_by_id('vplf'))
    # WW(driver, 10).until(EC.presence_of_element_located((By.ID, "vplf"))) #vpl_html5_api
    tutorial_soup = BS(driver.page_source, 'html.parser')
    print(tutorial_soup.find_all('div', attrs={'id': 'vpfi'}))
    # tutorial_code_soup = tutorial_soup.find_all('div', attrs={'class': 'code-toolbar'})
except Exception:
    pass

driver.quit()