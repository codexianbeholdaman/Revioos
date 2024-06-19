from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

GECKODRIVER_PATH = "/snap/bin/geckodriver"

driver_service = webdriver.FirefoxService(executable_path = GECKODRIVER_PATH)
driver = webdriver.Firefox(service=driver_service)
driver.get(f'https://rpgcodex.net/forums/threads/a-repository-for-codexian-reviews.150342/')

full_page = driver.page_source
with open('_all_pages.py', 'w') as all_pages:
    all_pages.write(f'all_pages = ["""\n{full_page}\n"""]')

driver.close()
