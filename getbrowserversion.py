from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://bing.com')

print('Firefox Driver Version: '+browser.capabilities['version'])

browser.close()
browser.quit()