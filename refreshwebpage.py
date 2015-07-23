import time
from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://wikipedia.org')
time.sleep(3)

browser.refresh()
time.sleep(2)

browser.close()
browser.quit()