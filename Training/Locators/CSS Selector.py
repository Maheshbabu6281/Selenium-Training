import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.facebook.com/r.php?entry_point=login')
time.sleep(2)
driver.find_element('css selector','input[name="firstname"]').send_keys('mahesh')
time.sleep(2)
driver.find_element('css selector','input[name="lastname"]').send_keys('vanamala')
time.sleep(2)
driver.find_element('css selector','input[aria-label="Mobile number or email address"]').send_keys('6281083641')
time.sleep(2)
driver.close()