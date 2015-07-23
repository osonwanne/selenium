from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')

try:
	driver.find_element_by_xpath("//a[@class='_Gs']")
	print('Test Passed: Link text class by XPath found')

except Exception as e:
	print('Exception found',format(e))

driver.close()
driver.quit()