from selenium import webdriver
#This is to import a module to use your keyboard
from selenium.webdriver.common.keys import Keys
#These are to use the delay parametrs so that you can wait before you do something
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#This is to use action functionalities such as drag and drop, or double click
from selenium.webdriver.common.action_chains import ActionChains
import requests, pprint, os
driver = webdriver.Chrome()
driver.get('https://orteil.dashnet.org/cookieclicker/')
#waiting for passed argument seconds till the website has loaded
driver.implicitly_wait(40)
cookies = driver.find_element_by_id('bigCookie')
cookie_count = driver.find_element_by_id('cookies')
# This means that we want to upgrade the productPrice1 first: which is more expensive as per the website
items = [driver.find_element_by_id('productPrice'+str(i)) for i in range(1,-1,-1)]#The last bit means that it will go from 1 to 0
item_names = [driver.find_element_by_id('productName'+str(j))for j in range(1,-1,-1)]
product_owned = [driver.find_element_by_id('productOwned'+str(k))for k in range(1,-1,-1)]
actions = ActionChains(driver)# The ActionChain module is going to act on the passed parameter
actions.click(cookies)# This is not a command to click but rather a cue to click. If the actions.preform() isn't called, no action will be performed
for i in range(150):
	actions.perform()
	#When running, the count has a bunch of texts. Since we need the number only, we split it and store in a variable
	count = int(cookie_count.text.split(" ")[0])# count is how much we have
	for item in items:
		price = int(item.text)#How much is required to upgrade
		if item == items[0]:
			if price <= count:
				upgrade_actions = ActionChains(driver)
				upgrade_actions.move_to_element(item)
				upgrade_actions.click(item)
				upgrade_actions.perform()
				which_item = items.index(item)
				print('Number of items: '+str(item.text)+'\nThe product name is: '+ str(item_names[which_item].text)+'\nThis many items:'+ str(product_owned[which_item].text)+"\n========Line======")
		elif item == items[1]:
			print(str(item_names[0].text)+" is not found")
			upgrade_actions = ActionChains(driver)
			upgrade_actions.move_to_element(item)
			upgrade_actions.click(item)
			upgrade_actions.perform()
			which_item = items.index(item)
			print('Number of items: '+str(item.text)+'\nThe product name is: '+ str(item_names[which_item].text)+'\nThis many items:'+ str(product_owned[which_item].text)+"\n========Line======")