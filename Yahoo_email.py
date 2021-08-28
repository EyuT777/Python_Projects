#!python3
#This script uses infromation to login from cookies. To see how this is done. Refer to 'Loading and Saving Cookies.py'
import  sys, time, pickle, os
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
start = time.time()
os.makedirs('Cookies', exist_ok = True)
try:
	def save_cookie(location = '.\\cookies.txt'):
		(driver.get_cookies, open(location,'wb'))
		pickle.dump(driver.get_cookies(),open(location,'wb'))
	def load_cookies(driver, location = '.\\cookies.txt'):
		loading_cookies = pickle.load(open('cookies.txt','rb'))
		driver.delete_all_cookies()
		driver.get('https://google.com')
		for cookie in loading_cookies:
			driver.add_cookie(cookie)

	yahoo_login = 'https://mail.yahoo.com/'
	driver = webdriver.Chrome()
	load_cookies(driver)
	driver.get(yahoo_login)

	#wait 10 seconds before executing the next command
	driver.implicitly_wait(10)

	try:
		compose = driver.find_element_by_xpath('//a[@role = button]')
	except:
		compose = driver.find_element_by_link_text('Compose')
	compose.click()

	driver.implicitly_wait(10)

	try:
		recepient = driver.find_element_by_id('message-to-field')
		print('id worked')
		recepient.send_keys('[enter destination email]')
	except:
		recepient = driver.find_element_by_xpath('//input[@type = text]')
		recepient.send_keys('mickeytese@gmail.com')
		print('xpath worked')
	try:
		subject = driver.find_element_by_class_name('p_R')
		sub_input = subject.find_element_by_tag_name('input')
		sub_text = sub_input.find_element_by_class_name('q_T y_Z2hYGcu je_0 jb_0 X_0 N_fq7 G_e A_6EqO C_Z281SGl ir_0 P_0 bj3_Z281SGl b_0 j_n d_72FG em_N')
		sub_text.send_keys('This is Hello Again')
	except:
		subject = driver.find_element_by_xpath("//input[@aria-label = 'Subject']")
		subject.send_keys('This is Hello From a bot ;)')
		print('xpath worked')
	else:
		print('There is no value element named \"Subject\"')
	driver.implicitly_wait(5)
	try:
		body = driver.find_element_by_css_selector("div[aria-label = 'Message Body']")
	except:
		body = driver.find_element_by_xpath('//div[@role = "textbox"]')
		print('xpath worked')
	body.send_keys('Hey!\nJust wanted to say Hello. I look forward to hearing form you ;).')
	body.send_keys(Keys.CONTROL+Keys.RETURN)

	final = time.time() - start
	print(final)
except Exception as e:
	print('Failed ', str(e))
	driver.quit()

