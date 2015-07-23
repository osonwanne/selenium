import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://wikipedia.org')

# searches for topmost html tag
elm = browser.find_element_by_tag_name('html')

elm.send_keys(Keys.END)
time.sleep(2)

elm.send_keys(Keys.HOME)
time.sleep(1)

browser.close()
browser.quit()