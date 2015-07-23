from selenium import webdriver

driver = webdriver.Firefox()
driver.get('http://google.com')

try:
	driver.find_element_by_id('gbw')
	print('Test Pass: ID found')

except Exception as e:
	print("Exception found",format(e))

driver.close()

driver.quit()