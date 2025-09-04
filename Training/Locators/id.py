import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach',True)
driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)

driver.find_element('id','user-name').send_keys('standard_user')
time.sleep(1)
driver.find_element('id','password').send_keys('secret_sauce')
time.sleep(1)
driver.find_element('id','login-button').click()
time.sleep(4)
driver.find_element('id','react-burger-menu-btn').click()
time.sleep(1)
driver.find_element('id','logout_sidebar_link').click()

# driver.get('https://testautomationpractice.blogspot.com/')
# driver.find_element('id','name').send_keys('mahesh')
# time.sleep(1)
# driver.find_element('id','email').send_keys('mahesh1234@gmail.com')
# time.sleep(1)
# driver.find_element('id','phone').send_keys('9705631149')
# time.sleep(1)
# driver.find_element('id','textarea').send_keys('benaglore')
# time.sleep(1)
# driver.find_element('id','male').click()
# time.sleep(1)
# driver.find_element('id','monday').click()
# time.sleep(2)



