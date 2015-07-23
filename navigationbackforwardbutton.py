import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()
browser.get('http://google.com')

elem = browser.find_element_by_link_text('About')
time.sleep(2)

elem.click()
time.sleep(3)

browser.back()
time.sleep(2)

browser.forward()
time.sleep(1)

browser.close()
browser.quit()