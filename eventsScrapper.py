import requests
from bs4 import BeautifulSoup

"""
This module is a web scrapper that sends a request to https://www.onthisday.com/ and pulls
historic event data
"""

def generate_url(month, day):
    url = 'https://www.onthisday.com/day/{month}/{day}'
    return url
