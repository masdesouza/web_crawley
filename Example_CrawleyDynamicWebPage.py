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
 
print(html)'''


from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
url = 'https://angular.io/' 
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(url) 
 
print(driver.page_source)


