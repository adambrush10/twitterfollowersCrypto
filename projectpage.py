# app2.py
import streamlit as st
#from main import *
#import main
from APIcallFunctions import *
from calculategrowth import *
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import datetime
from numpy import mean
import time
import plotly.express as px

data5 = Rate_of_Change_Project().sort_values(by="Rates of Change", ascending=False)
data2 = Rate_of_Change_Sector()
data5 = data5.reset_index()
data3 = Rate_of_Change_subSector()

fig = go.Figure(data=[go.Table(
    header=dict(values=list(data5.columns),
                fill_color='#1d9bf0',
                line_color="#313233",
                height = 50,
                font=dict(color="white", size=24),
                align='center'),
    cells=dict(values=[data5["Project"], data5["Rates of Change"]],
               fill_color='#17181c',
               line_color="#313233",
               height = 50,
               font=dict(color="white", size=18),
               align='center'))
])
fig = fig.update_layout(width=800, height=5000)
#outputfig = fig.show()







def app():
    #st.set_page_config(layout="wide")

    st.markdown("<h1 style='text-align: center; color: white;'>Crypto Twitter Analytics</h1>", unsafe_allow_html=True)
    st.write('An Analysis of the average daily growth in followers for the Primary Accounts of Notable Crypto Projects')
    st.write('Categorized by Sector and Sub Sector. View Specific projects growth on the Projects Statistics Page')
    col1, col2= st.columns([1,2])

    with col1:
        st.subheader("Average Rate of Change by Sector")
        st.dataframe(data=data2)
        st.subheader("Average Rate of Change by sub Sector")
        st.write(data3) 

    with col2:
        #st.subheader("Average Rate of Change by Project")

        # Plot!
        st.plotly_chart(fig, use_container_width=False)    #, use_container_width=True
        #st.write(fig)
        # st.dataframe(data=data5, width=1200, height=1500) 
