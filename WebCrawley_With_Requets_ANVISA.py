#Project of scraping data from ANVISA website

'''
1) Get the data from the website "Consulta Anvisa"
2) Get the data from the website "Consulta Anvisa" using the requests library
3) In the website create a list of all menu items

'''
import requests

url = "https://consultas.anvisa.gov.br/#/saude/"
response = requests.get(url)
print(response.status_code)
print(len(response.text))
page_content = response.text
print(page_content[:1000])

with open('anvisa.html', 'w', encoding='utf-8') as f:
    f.write(page_content)





