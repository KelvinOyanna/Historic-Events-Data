from extract_export import create_events_data, write_raw_data
from transform_load import transformData, load_data_to_db, write_tranformed_data
import datetime as dt

start_date = dt.date(2020, 1, 1)
end_date = dt.date(2020, 1, 7)

if __name__ == '__main__':
    # Scrape events data
    events_data = create_events_data(start_date, end_date)
    # write raw scraped data to csv file
    write_raw_data(events_data)
    #transform the scraped data
    transformed_data = transformData(events_data)
    # Write transformed data to csv file
    write_tranformed_data(transformed_data)
    # load the transformed data to postgresql database
    load_data_to_db(transformed_data)
    


