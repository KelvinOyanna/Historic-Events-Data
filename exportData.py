from typing import Iterator
import datetime as dt
import eventsScrapper as scrapper
import pandas as pd 
import os


def date_range(start_date: dt.date, end_date: dt.date) -> Iterator[dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)

def create_events():
    events_df = pd.DataFrame()
    start_date = dt.date(2020, 1, 1)
    end_date = dt.date(2020, 1, 10 )
    for date in date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        event_rows = scrapper.events_of_the_day(month, date.day)
        month_df = pd.DataFrame(event_rows, columns=['Events'])
        events_df = events_df.append(month_df)
    return events_df

def export_data():
    if not os.path.exists(os.path.abspath('./') + '\RawEventsData'):
        os.mkdir('RawEventsData')
    events_df = create_events()
    events_df.to_csv('RawEventsData/events.csv', index= False)
# Export data to json