from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

browser = webdriver.Firefox()
browser.get('http://wikipedia.org')

elm = browser.find_element_by_link_text('Wikiversity')
elm.click()
browser.implicitly_wait(2)

print(browser.current_url)

browser.close()
browser.quit()