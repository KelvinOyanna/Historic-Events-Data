import requests
from bs4 import BeautifulSoup

"""
This module is a web scrapper that sends a request to https://www.onthisday.com/ and pulls
historic event data
"""

def generate_url(month, day):
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def events_of_the_day(month, day):
    """
    Return the events of a given day
    """
    url = generate_url(month, day)
    page = get_page(url)
    raw_events = page.find_all(class_ = "event")
    events = [event.text for event in raw_events]
    return events
