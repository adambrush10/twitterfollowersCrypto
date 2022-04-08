# app1.py
import streamlit as st
#from main import *
from APIcallFunctions import *
from calculategrowth import *
import urllib.request
from xml.dom.xmlbuilder import Options
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import time
import plotly.graph_objects as go
import plotly.express as px

# List of all available projects (need to update regularly as new ones are added)
projectlist = ["Premia.Finance","PoolTogether","Luna","Aave","Zcash","Monero","USDC","USDT","Fantom","Nexus Mutual","Crypto Punks","Bored Ape Yacht Club","NessGraphics","SushiSwap","Dogami","Bitcoin","Ethereum",]
data6 = PullProject_info()  #attempting to run this function outside of the statsfromoption function to decrease load times


#def LoadFromOption(selection):
   # data0 = lineChart2(selection)
  #  return data0

def StatsFromOption(selection):

    #data6 = PullProject_info()
    results = data6.loc[selection]
    new = results.to_frame()
    newString = new.astype(str)
    return newString


## load image
def LoadImage(selection):
    data7 = data6.transpose()
    data8 = data7[selection]
    pic = data8.iloc[5]
    urllib.request.urlretrieve(pic,"logo.jpg")
    im = Image.open("logo.jpg")
    return im




def app():
    st.title("Crypto Twitter Analytics")
    data_load_state = st.text('Loading data...')
    data_load_state.text('This site aims to provide actionable investing insights for the growth of Twitter Handles among various projects in the Crypto space')
    option = st.selectbox(
    'Select Protocol', projectlist)

    st.write('You selected:', option)

    col1, col2 = st.columns([1,2])


    with col2:
        st.subheader('Twitter Follower Activity by Project')
        st.plotly_chart(lineChart2(option))

        #st.subheader("Average Rate of Change by sub Sector")
        #st.write(data3)  
 

    with col1:
        st.subheader("statistics for project")
        st.image(LoadImage(option))
        with st.spinner('Loading...'):
            time.sleep(2)
        
        st.write(StatsFromOption(option))

        st.subheader("Average Rate of Change within the Sector")
        st.write(ProjectbySector(option))
        