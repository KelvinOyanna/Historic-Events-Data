import requests
from typing import List, Iterator
from bs4 import BeautifulSoup
import pandas as pd

"""
This module is a web scrapper that sends a request to https://www.onthisday.com/ and pulls
historic event data
"""

def generate_url(month: str, day: str) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def get_page(url: str) -> Iterator[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    """
    Return the events of a given day
    """
    url = generate_url(month, day)
    page = get_page(url)
    raw_events = page.find_all(class_ = "event")
    events = [event.text for event in raw_events]
    event_rows = [row for row in events]
    return event_rows
