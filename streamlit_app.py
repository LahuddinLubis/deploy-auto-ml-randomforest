import streamlit as st
import pandas as pd

st.title('🎈 Machine Learning App')
st.info('Prediksi Spesies Penguin dengan Algoritma Random Forest')

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
