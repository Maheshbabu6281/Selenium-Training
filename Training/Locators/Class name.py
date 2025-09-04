import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

driver.get('https://testautomationpractice.blogspot.com/')
time.sleep(2)

driver.find_element('class name', 'form-control').send_keys('sai ganesh')
time.sleep(2)
driver.find_element('class name','form-control').send_keys('babu')
time.sleep(2)