import time
from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('xpath','')
