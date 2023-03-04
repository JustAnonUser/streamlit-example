import streamlit as st
import pandas as pd
import numpy as np


st.title('Hey you!...')
st.title('...')
st.title('..')
st.title('.')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('I´m trying to learn this shit')
# Load 10,000 rows of data into the dataframe.
data = load_data(20000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Streamlit es raro...')
data = load_data(8000)
# Create a text element and let the reader know the data is loading.
data_load_state2 = st.text('That text was supposed to change...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state2.text('Hope it did it...Ahora algo cool, espero...')

