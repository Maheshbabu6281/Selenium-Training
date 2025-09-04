import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.flipkart.com/')
driver.find_element('xpath','//span[@text() =Mobiles & Tablets]').click()
time.sleep(2)
