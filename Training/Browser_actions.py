#initiliase the browser object
import time

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
driver = webdriver.Chrome(opts)

#launch the application
driver.get("https://www.myntra.com/")
time.sleep(2)

# #maximise window
# driver.maximize_window()
# time.sleep(2)
#
# #minimise window
# driver.minimize_window()
# time.sleep(2)
#
# #to go back
# driver.back()
# time.sleep(2)
#
#
# #to go formard
# driver.forward()
# time.sleep(2)
#
# #to refresh the page
# driver.refresh()
# time.sleep(2)
#
# print(driver.title)
# print(driver.current_url)
# print(driver.name)

# driver.save_screenshot('mynthra_screnshot.png')
driver.save_screenshot(r'C:\Users\Mahesh\PycharmProjects\Selenium_traing\Files\mym_ss.png')

from selenium import webdriver
opts = webdriver.ChromeOptions()
opts.add_experimental_option
