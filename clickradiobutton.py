from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

# browser/driver object
browser = webdriver.Firefox() 
# instance of Firefox
browser.get('http://www.zkoss.org/zkdemo/input/radio_button') 

for ii in browser.find_elements_by_xpath('//*[@type="radio"]'):
	ii.click()

browser.implicitly_wait(6)

browser.close()
browser.quit()