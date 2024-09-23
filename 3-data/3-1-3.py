import pandas as pd
import streamlit as st
import numpy as np

customers = pd.read_csv('https://raw.githubusercontent.com/mafudge/datasets/master/customers/customers.csv')

gender = st.radio("Select Gender:", ["M","F",])
cols = st.multiselect("Select Columns:", customers.columns)
gender_index = customers['Gender']==gender

st.dataframe(customers[gender_index][cols])