import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')
st.info('Prediksi Spesies Penguin dengan Algoritma Random Forest')

# Load dataset
with st.expander('Dataset'):
  st.write('Row Dataset')
  df = pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv")
  df

  st.write('Feature Dataset (X)')
  X = df.drop('species', axis=1)
  X

  st.write('Label Dataset (y)')
  y = df.species
  y

# Data Visualisation
with st.expander('Data Visualisation'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')

# Data Preparation
with st.sidebar:
  st.header('Input Feature (X)')
  island = st.selectbox('Island', ('Biscoe', 'Dream', 'Torgersen'))
  gender = st.selectbox('Gender', ('Male', 'Female'))
  bill_length_mm = st.slider('Bill Length (mm)', 32.1, 59.6, 43.9)
  bill_depth_mm = st.slider('Bill Depth (mm)', 13.1, 21.5, 17.2)
  flipper_length_mm = st.slider('Flipper Length (mm)', 172.0, 231.0, 201.0)
  body_mass_g = st.slider('Body Mass (g)', 2700.0, 6100.0, 420)
