from xml.dom.xmlbuilder import Options
import pandas as pd
import numpy as np
import datetime
import streamlit as st
from calculategrowth import *
from APIcallFunctions import *
import homepage
#from homepage import *
import projectpage
#from projectpage import *
from numpy import mean
import matplotlib.pyplot as plt
from PIL import Image
import time
import urllib.request
import plotly.graph_objects as go


st.set_page_config(layout="wide")

PAGES = {
    "Industry Overview": projectpage,
    "Project Statistics": homepage
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()




### run streamlit by streamlit run main.py

#st.title("Crypto Twitter Analytics")


# Create a text element and let the reader know the data is loading.
#data_load_state = st.text('Loading data...')


# List of all available projects (need to update regularly as new ones are added)
#projectlist = ["Premia.Finance","PoolTogether","Luna","Aave","Zcash","Monero","USDC","USDT","Fantom","Nexus Mutual","Crypto Punks","Bored Ape Yacht Club","NessGraphics","SushiSwap","Dogami","Bitcoin","Ethereum",]

# data0 = lineChart(ProjectName)
data = Avg_Change_by_Name()
#data2 = Rate_of_Change_Sector()
#data3 = Rate_of_Change_subSector()
data4 = Rate_of_Change_type()
#data5 = Rate_of_Change_Project()
#data6 =ProjectbySector(selection)
#data6 = PullProject_info()

#data_load_state.text('This site aims to provide actionable investing insights for the growth of Twitter Handles among various projects in the Crypto space')

#fig = go.Figure(data=data5)
#outputfig = fig.show()

## LOAD MAIN CHART

 
#def LoadFromOption(selection):
#    data0 = lineChart(selection)
 #   return data0

#option = st.selectbox(
 #   'Select Protocol', projectlist)

#st.write('You selected:', option)

## Load column 1 statistics


# data6 = PullProject_info()  #attempting to run this function outside of the statsfromoption function to decrease load times



#def StatsFromOption(selection):

    #data6 = PullProject_info()
 #   results = data6.loc[selection]
  #  new = results.to_frame()
   # newString = new.astype(str)
    #return newString
    
## load image
#def LoadImage(selection):
#    data7 = data6.transpose()
#    data8 = data7[selection]
#    pic = data8.iloc[5]
#    urllib.request.urlretrieve(pic,"logo.jpg")
#    im = Image.open("logo.jpg")
#    return im





















#LAYOUT OF THE WEB APP 



#col1, col2, col3 = st.columns([1,3,1])


#with col2:
 #   st.subheader('Twitter Follower Activity by Project')
  #  st.pyplot(LoadFromOption(option).figure)

   # st.subheader("Average Rate of Change by sub Sector")
    #st.write(data3)  

#with col3:
 #   st.subheader("Average Rate of Change by Type")
  #  st.write(ProjectbySector(option))

   # st.subheader("Average Rate of Change by Sector")
    #st.write(data2) 

#with col1:
 #   st.subheader("statistics for project")
  #  st.image(LoadImage(option))
   # with st.spinner('Loading...'):
    #    time.sleep(2)
    
   # st.write(StatsFromOption(option))
   # st.write("Primary Account link")


    # st.subheader('Twitter Follower Account Rate of Change')
    # st.write(data)
 



#st.subheader("Average Rate of Change by Type")
#st.write(data4) 

#st.subheader("Average Rate of Change by Project")
#st.write(data5) 

