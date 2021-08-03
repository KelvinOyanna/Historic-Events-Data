from pandas.core.frame import DataFrame
from exportData import export_data
import pandas as pd
import psycopg2
import datetime as dt
from typing import Dict
from dotenv import dotenv_values

# Function to get database credencials from the environment virable
def credentials() -> Dict:
    config = dotenv_values('.env')
    return config

def transformData() -> DataFrame:
    # A helper function to extract the day and month in history an event occoured
    def extractMonthDay(date_coln: str) ->str:
        date_coln = dt.date(date_coln).strftime('%d %B')
        return date_coln
    # A helper function to extract the year an event occured
    def extractYearEventOccoured(event):
        year = event.split(' ')[0]
        return year
    # A helper function to extract only the event information
    def extractEvent(event):
        event = ' '.join(event.split(' ')[1:])
        return event
    try:
        events_data = pd.read_csv('/RawEventsData/events.csv') #  Read event data from event file
        events_data['Date In History'] = events_data['Date'].apply(extractMonthDay)
        events_data['Year Occured'] = events_data['Event'].apply(extractYearEventOccoured)
        events_data['Event'] = events_data['Event'].apply(extractEvent)
        return events_data[['Date In History', 'Year Occured', 'Event']]
    except FileNotFoundError:
        print('Kindly check that events.csv & its folder exist and try again')
    



#def loadToPostgres():

df = transformData()
#print(df.head())