from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://google.com')

elm = browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')

browser.close()
browser.quit()