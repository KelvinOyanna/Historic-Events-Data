from typing import Iterator
import datetime as dt
import eventsScrapper as scrapper
import pandas as pd 
import os

# Function to create a range of date within which data is to be extracted
def date_range(start_date: dt.date, end_date: dt.date) -> Iterator[dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)

# Function to create event for the range of date from above
def create_events_data(start_date, end_date):
    """
    This function generate the month and day that is passed into the request made 
    from the eventScrapper function to the website - www.onthisday.com
    """
    events_df = pd.DataFrame()
    for date in date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        event_rows = scrapper.events_of_the_day(month, date.day)
        month_df = pd.DataFrame(event_rows, columns=['Event'])
        month_df['Date'] = date
        events_df = events_df.append(month_df)
    return events_df

# A function to export data as is, to an external csv file
def write_raw_data(events_data):
    """
    This function uses the os module to create a new directory - RawEventsData, if it
    does not currently exist where it saves the exported data.
    """
    if os.path.exists(os.path.abspath('./') + '\RawEventsData'):
        events_data.to_csv('RawEventsData/events.csv', index= False)
        print('raw data sucessfully written to a csv file')
    else:
        os.mkdir('RawEventsData')
        events_data.to_csv('RawEventsData/events.csv', index= False)
        print('raw data sucessfully written to a csv file')
