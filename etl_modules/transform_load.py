from pandas.core.frame import DataFrame
import pandas as pd
import psycopg2
from sqlalchemy import create_engine, engine
from datetime import datetime as dt
from typing import Dict
from dotenv import dotenv_values
import os

# function to get database credentials from the environment variable file(.env), establish
# a connection to the database and renturn a connection engine.
def db_connection():
    config = list(dotenv_values('.env').values())
    connection_string = f"postgresql+psycopg2://{config[0]}:{config[1]}@localhost/{config[2]}"
    try:
        engine = create_engine(connection_string)
        return engine
    except ConnectionError:
        print('Unable to establish a connection to the database. Please check your database credentials')

# A function to process/transform the scrapped data before it's loaded to a database
def transformData(events_data):
    # A helper function to extract the day and month in history, an event occoured
    def extractMonthDay(date_coln):
        month_day = dt.strptime(str(date_coln), '%Y-%m-%d').date().strftime('%d %B')
        return month_day
    # A helper function to extract the year an event occured
    def extractYearEventOccoured(event):
        year = event.split(' ')[0]
        if len(year) < 4:
            return year + 'BC'
        else:
            return year
    # A helper function to extract only the event information
    def extractEvent(event):
        event = ' '.join(event.split(' ')[1:])
        return event

    events_data['Month_Day'] = events_data['Date'].apply(extractMonthDay)
    events_data['Year_Occured'] = events_data['Event'].apply(extractYearEventOccoured)
    events_data['Event'] = events_data['Event'].apply(extractEvent)
    return events_data[['Month_Day', 'Year_Occured', 'Event']]


# Function to write the processed data to an external file   
def write_tranformed_data(events_data):
    try:
        if os.path.exists(os.path.abspath('./') + '\ProcessedData'):
            events_data.to_csv('ProcessedData/events.csv', index= False)
            print('transformed data sucessfully written to file...')
        else:
            os.mkdir('ProcessedData')
            events_data.to_csv('ProcessedData/events.csv', index= False)
            print('transformed data sucessfully written to file...')
    except SystemError:
        print('Could not write the data to an external file')

# Function to load data to a postgresql database
def load_data_to_db(events_data):
    engine = db_connection()
    try:
        events_data.to_sql('events_history', con = engine, if_exists= 'append', index= False)
        print('transformed data sucessfully loaded to database...')
    except ConnectionError:
        print('Unable to establish a connection to the database. Please check your database credentials')
