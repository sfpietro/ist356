import pandas as pd
import streamlit as st
import numpy as np

link = 'https://raw.githubusercontent.com/mafudge/datasets/refs/heads/master/delimited/webtraffic.log'
log = pd.read_csv(link, sep=" ",header=3, skiprows=3)
st.dataframe(log)
slow_filter = (log['time-taken'] > 500 & (log['sc-status']==200))
st.dataframe(slow_filter)