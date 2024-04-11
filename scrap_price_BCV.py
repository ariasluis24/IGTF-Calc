# Imported requests, urllib3 & BeatifulSoup to successfully scrap the price of the BCV Page
import requests, urllib3
urllib3.disable_warnings()
from bs4 import BeautifulSoup

# Scrap part
page_to_scrape = requests.get('https://www.bcv.org.ve', verify=False)
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')
parent_container = soup.find(id='dolar')

# Formating part
list_BCV = list(parent_container.find('strong').text.strip()) #  Result = ['3', '6', ',', '1', '8', '8', '3', '0', '0', '0', '0']
list_BCV.remove(',') # Result = ['3', '6', '1', '8', '8', '3', '0', '0', '0', '0']
list_BCV.insert(2, '.') #Result = ['3', '6', '.', '1', '8', '8', '3', '0', '0', '0', '0']

str_BCV = ''.join(list_BCV) # Formating list into a single string 36.18830000.
price_BCV = float(str_BCV) # Casting string into a float.

print(price_BCV) # Result = 36.1883   