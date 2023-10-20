'''
We can parse the JSON string to extract the necessary data, or others ways to crawley dynamic web pages are two:
    1) Manually locating the data and parsing JSON string.

    2) Using headless browsers to execute the page’s internal JavaScript
      (e.g., Selenium or Pyppeteer, an unofficial Python port of Puppeteer).

To need install Selenium and Webdriver Manager, to execute in bash or cmd:
pip install selenium webdriver-manager
     

      
'''
# Dynamic Web Scraping With Python Using Beautiful Soup


# Scraping Dynamic Web Pages in Python Using Selenium

'''import requests 
 
url = 'https://angular.io/'  

 
response = requests.get(url) 
 
html = response.text 
 
print(html)


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
url = 'https://angular.io/'
#url = 'https://www.lottoland.com/br'  
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(url) 
 
print(driver.page_source)

# Scraping Dynamic Web Pages in Python Using Selenium

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
# instantiate options 
options = webdriver.ChromeOptions() 
 
# run browser in headless mode 
options.headless = True 
 
# instantiate driver 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load website 
url = 'https://angular.io/' 
 
# get the entire website content 
driver.get(url) 
 
# select elements by class name 
elements = driver.find_elements(By.CLASS_NAME, 'text-container') 

for title in elements: 
	# select H2s, within element, by tag name 
	heading = title.find_element(By.TAG_NAME, 'h2').text 
	# print H2s 
	print(heading)'''

#How to Scrape Infinite Scroll Web Pages With Selenium and Python

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
import time 
 
options = webdriver.ChromeOptions() 
options.headless = True 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install()), options=options) 
 
# load target website 
url = 'https://scrapingclub.com/exercise/list_infinite_scroll/' 
 
# get website content 
driver.get(url) 
 
# instantiate items 
items = [] 
 
# instantiate height of webpage 
last_height = driver.execute_script('return document.body.scrollHeight') 
 
# set target count 
itemTargetCount = 20 
 
# scroll to bottom of webpage 
while itemTargetCount > len(items): 
	driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
 
	# wait for content to load 
	time.sleep(1) 
 
	new_height = driver.execute_script('return document.body.scrollHeight') 
 
	if new_height == last_height: 
		break 
 
	last_height == new_height 
 
	# select elements by XPath 
	elements = driver.find_elements(By.XPATH, "//div[@class='card-body']/h4/a") 
	h4_texts = [element.text for element in elements] 
 
	items.extend(h4_texts) 
 
	# print title 
	print(h4_texts)