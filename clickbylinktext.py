from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get('http://google.com')

elm = browser.find_element_by_link_text('About')
browser.implicitly_wait(5)
elm.click()

browser.close()
browser.quit()