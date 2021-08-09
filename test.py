import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://www.abokifx.com/home_bdc_rate'
web = requests.get(url)

soup = BeautifulSoup(web.content, 'html.parser')
table = soup.find_all('table')[0]
#data = pd.read_html(table)[0]

print(table)