from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time, pprint,shelve, pickle
def save_cookie(location = '.\\cookies.txt'):
	pickle.dump(driver.get_cookies(), open(location,'wb'))
def load_cookies(driver, location = '.\\cookies.txt'):
	cookies = pickle.load(open(location,'rb'))
	driver.delete_all_cookies()
	driver.get('https://google.com')
	for cookie in cookies:
		driver.add_cookie(cookie)

#initialize your webdriver
driver = webdriver.Chrome()

#get an address and navitage towards it

driver.get('https://login.yahoo.com')
#Saves cookies to the current directory
save_cookie()
# load_cookies(driver)


