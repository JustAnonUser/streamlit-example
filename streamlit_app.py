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
data = load_data(21500)
# Create a text element and let the reader know the data is loading.
data_load_state2 = st.text('That text was supposed to change...')
# Load 10,000 rows of data into the dataframe.
data = load_data(23000)
# Notify the reader that the data was successfully loaded.
data_load_state2.text('Hope it did it...Ahora una gráfica chida')


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)


# Create a text element and let the reader know the data is loading.
data_load_state3 = st.text('Una parte secreta')

import streamlit as st
import streamlit_authenticator as stauth
names = ['Andres Jaquez','Ernesto Valenciana']
usernames = ['jaquez','valenciana']
passwords = ['andres','ernesto']

hashed_passwords = stauth.hasher(passwords).generate()
authenticator = stauth.authenticate(names,usernames,hashed_passwords,
    'some_cookie_name','some_signature_key',cookie_expiry_days=30)
name, authentication_status = authenticator.login('Login','main')
if authentication_status:
    st.write('Pasaste la prueba! *%s*' % (name))
    st.title('Croe que puedo programar aqui')
elif authentication_status == False:
    st.error('Datos incorectos')
elif authentication_status == None:
    st.warning('Ingresa con tu usuario y contraseña')

if st.session_state['authentication_status']:
    st.write('Holap! *%s*' % (st.session_state['name']))
    st.title('Entraste!')
elif st.session_state['authentication_status'] == False:
    st.error('Datos incorectos')
elif st.session_state['authentication_status'] == None:
    st.warning('Ingresa con tu usuario y contraseña')
