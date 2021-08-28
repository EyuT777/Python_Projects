from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time, pprint

#os.chdir('C:\\Users\\Eyobed T. Kebede\\Desktop\\New Files\\Python Files\\Atom files\\Chapter 11')
browser = webdriver.Chrome()
(type(browser))
header_link = {}
text_ref = 'http://inventwithpython.com'
my_ref = 'https://www.google.com/search?q=SEARCH_TERM_HERE'
ref2  ='https://practice.geeksforgeeks.org/courses/?ref=gfg_header'
tim_ref = 'https://techwithtim.net'
browser.get(tim_ref)
search = browser.find_element_by_name('s')
search.clear()# To clear anything in the search bar, if any exist. Else it will append and not replace
search.send_keys('test')
search.send_keys(Keys.RETURN)
# If we try to search for the next term without the page loading, we might get an error. SO we wait about 10 seconds after searching to make another move
   #This needs better connection. Wait till morning
try:
    main = WebDriverWait(browser, 100).until(EC.presence_of_element_located((By.ID, 'main')))# THis is for the wait before searching for name,
    articles = main.find_elements_by_tag_name('article')
    for article in articles:
        print(article.text)
        titles = article.find_elements_by_class_name('entry-header')
        for title in titles:
            links = title.find_elements_by_tag_name('a')
            for link in links:
                date = title.text
                header_link[date] = link.get_attribute('href')
    pprint.pprint(header_link)
finally:
    browser.quit()
#time.sleep(10)# This waits 10 seconds before the browser is shut
