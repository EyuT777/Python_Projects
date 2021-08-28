from selenium import webdriver
from selenium import webdriver
#This is to import a module to use your keyboard
from selenium.webdriver.common.keys import Keys
#These are to use the delay parametrs so that you can wait before you do something
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#This is to use action functionalities such as drag and drop, or double clickimport requests, pprint, os
try:
	driver = webdriver.Chrome()
	driver.get('https://techwithtim.net')
	#Finding the link text that is denoted by the argument passed
	links = driver.find_element_by_link_text('Python Programming')# This finds the link that is represented by the argument
	links.click()#Clicks the link
	#There will be a max 30 sec wait, then we'll be taken to the intermediate programming section
	intermediate = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Intermediate')))# THis is for the wait before searching for name,
	intermediate.click()
	#another 30 sec wait, then we are taken to the get started button of the page to start the course.
	getting_started = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.ID,"sow-button-19310003")))
	getting_started.click()
	# to go back one step. Or to go to the main page, use the back fucntion as many times as the click function is used
	driver.back()
	driver.back()
	driver.back()
	# To go forward. The page is already loaded in the cache so you this process will be easily done
	driver.forward()
	driver.forward()
	driver.forward()
except:
	driver.quit()
	print('Time out error')