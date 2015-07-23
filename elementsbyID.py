from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://onecore.net')

ids = driver.find_elements_by_xpath('//*[@id]')

for ii in ids:
	print(ii.get_attribute('id'))

driver.close()

driver.quit()