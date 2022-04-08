import pandas as pd
import numpy as np
import datetime
import streamlit as st
from numpy import mean
# import matplotlib.pyplot as plt
import plotly.express as px

#This file is meant to organize growth into 5 groups. (twitter handle, sector, sub sector, type, and Project)



# ouputs a dict of % change in daily follower count in chronological order. Follower counts are collected daily from 3/25/22
def growth_by_handle():
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")

    #create classifications DataFrame
    classifications = df.head(5)

    #create classifications dict
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')

    #establish a list of twitter handles for keys 
    keysList = list(byTwitterHandleOBJECT.keys())



    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    growth_rate = np.exp(np.diff(np.log(datelist))) -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    percentagelist = [] 
    for x in growth_rate:
        for y in x:
            y = "{:.2%}".format(y)
            percentagelist.append(y)
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    res = {}
    for key in keysList:
        for value in new_plist:
            res[key] = value
            new_plist.remove(value)
            break  

    print(res)
    return res 



################################   create a function to organize growth by sector
def sectorGrowth():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()

    #turn the growth rate array into a string of percentages and name it new_plist
    percentagelist = []
    for x in growth_rate:
        for y in x:
            y = "{:.2%}".format(y)
            percentagelist.append(y)
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]

    #create a dictionary to turn into a df 
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            res[key] = value
            new_plist.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            byTwitterHandleOBJECT[key].append(value)
            new_plist.remove(value)
            break


    value = "Gaming "
    gaming = []
    
    for x in keysList:
        byTwitterHandleOBJECT.get(x, "Gaming ")
        if value in byTwitterHandleOBJECT.values():
            gaming.append(x)    
    resDF = pd.DataFrame.from_dict(res)
    sectorList = df.loc[0, :].values.tolist()
    # print(sectorList)
    sectorList.pop(0)
    resDF.iloc[0] = sectorList
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    sectorDF = pd.DataFrame()
    sectorDF["Sector"] = sectorList
    sectorDF["Rates of Change"] = new_plist
    ResultsSECTOR = sectorDF.groupby(by=["Sector"]).sum()
    print(ResultsSECTOR)
    return ResultsSECTOR


#create a function to organize growth by subsector
def SUBsectorGrowth():
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    percentagelist = []
    for x in growth_rate:
        for y in x:
            y = "{:.2%}".format(y)
            percentagelist.append(y)

    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            res[key] = value
            new_plist.remove(value)
            break

    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            byTwitterHandleOBJECT[key].append(value)
            new_plist.remove(value)
            break
    gaming = []
    for x in keysList:
        byTwitterHandleOBJECT.get(x, "Gaming ")
        if value in byTwitterHandleOBJECT.values():
            gaming.append(x)
    resSUBDF = pd.DataFrame.from_dict(res)
    SUBsectorList = df.loc[1, :].values.tolist()
    SUBsectorList.pop(0)
    resSUBDF.iloc[0] = SUBsectorList
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    SUBsectorDF = pd.DataFrame()
    SUBsectorDF
    SUBsectorDF["Sub Sector"] = SUBsectorList
    SUBsectorDF["Rates of Change"] = new_plist
    SUBsectorDF_results = SUBsectorDF.groupby(by=["Sub Sector"]).sum()
    print(SUBsectorDF_results)
    return SUBsectorDF_results


#create a function to organize growth by type

def TypeGrowth():
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    percentagelist = []
    for x in growth_rate:
        for y in x:
            y = "{:.2%}".format(y)
            percentagelist.append(y)

    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            res[key] = value
            new_plist.remove(value)
            break

    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            byTwitterHandleOBJECT[key].append(value)
            new_plist.remove(value)
            break
    gaming = []
    for x in keysList:
        byTwitterHandleOBJECT.get(x, "Gaming ")
        if value in byTwitterHandleOBJECT.values():
            gaming.append(x)
    resTYPEDF = pd.DataFrame.from_dict(res)
    TypeList = df.loc[2, :].values.tolist()
    TypeList.pop(0)
    resTYPEDF.iloc[0] = TypeList
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    TypeDF = pd.DataFrame()
    TypeDF
    TypeDF["Type"] = TypeList
    TypeDF["Rates of Change"] = new_plist
    TypeDF_results =  TypeDF.groupby(by=["Type"]).sum()
    print( TypeDF_results)
    return  TypeDF_results



#create a function to organize growth by Project

def ProjectGrowth():
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    percentagelist = []
    for x in growth_rate:
        for y in x:
            y = "{:.2%}".format(y)
            percentagelist.append(y)

    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            res[key] = value
            new_plist.remove(value)
            break

    for key in byTwitterHandleOBJECT:
        for value in new_plist:
            byTwitterHandleOBJECT[key].append(value)
            new_plist.remove(value)
            break
    gaming = []
    for x in keysList:
        byTwitterHandleOBJECT.get(x, "Gaming ")
        if value in byTwitterHandleOBJECT.values():
            gaming.append(x)
    resTYPEDF = pd.DataFrame.from_dict(res)
    ProjectList = df.loc[3, :].values.tolist()
    ProjectList.pop(0)
    resTYPEDF.iloc[0] = ProjectList
    new_plist = [percentagelist[i:i + len(growth_rate[1])] for i in range(0, len(percentagelist), len(growth_rate[1]))]
    ProjectDF = pd.DataFrame()
    ProjectDF
    ProjectDF["Project"] = ProjectList
    ProjectDF["Rates of Change"] = new_plist
    ProjectDF_results =  ProjectDF.groupby(by=["Project"]).sum()
    print( ProjectDF_results)
    return  ProjectDF_results



# function to display a df of the average change in followers sorted by twitter name   --- future versions to display the option to view averages of time periods (24hr, 7day 30day, etc.)
@st.cache
def Avg_Change_by_Name():
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate = growth_rate.tolist()
    averages = []
    for k in growth_rate:
        avg = mean(k)
        averages.append(avg)
    percentagelist = []
    for x in averages:
        x = "{:.2%}".format(x)
        percentagelist.append(x)
    dictionary = dict(zip(keysList, percentagelist))
    AveragebyHandleDF = pd.DataFrame
    AveragebyHandleDF = pd.DataFrame.from_dict(dictionary, orient='index', columns = [ "Rate of Change"])
    return AveragebyHandleDF



def Rate_of_Change_Sector():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)

    #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    sectorList = df.loc[0, :].values.tolist()
    sectorList.pop(0)

    #create the dataframe   
    MeanSectorDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    MeanSectorDF["Sector"] = sectorList
    MeanSectorDF = MeanSectorDF.groupby(by=["Sector"]).mean()
    changelist = MeanSectorDF['Rate of Change'].tolist()
    mean_plist = []
    for x in changelist:
        x = "{:.2%}".format(x)
        mean_plist.append(x)
    MeanSectorDF["Rates of Change"] = mean_plist
    MeanSectorDF = MeanSectorDF.drop(columns =["Rate of Change"])
    return MeanSectorDF

def Rate_of_Change_subSector():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)

    #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    subsectorList = df.loc[1, :].values.tolist()
    subsectorList.pop(0)

    #create the dataframe   
    MeansubSectorDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    MeansubSectorDF["Sub Sector"] = subsectorList
    MeansubSectorDF = MeansubSectorDF.groupby(by=["Sub Sector"]).mean()
    changelist = MeansubSectorDF['Rate of Change'].tolist()
    mean_plist = []
    for x in changelist:
        x = "{:.2%}".format(x)
        mean_plist.append(x)
    MeansubSectorDF["Rates of Change"] = mean_plist
    MeansubSectorDF = MeansubSectorDF.drop(columns =["Rate of Change"])
    return MeansubSectorDF

def Rate_of_Change_type():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)

    #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    typeList = df.loc[2, :].values.tolist()
    typeList.pop(0)

    #create the dataframe   
    typeDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    typeDF["Type"] = typeList
    typeDF = typeDF.groupby(by=["Type"]).mean()
    changelist = typeDF['Rate of Change'].tolist()
    mean_plist = []
    for x in changelist:
        x = "{:.2%}".format(x)
        mean_plist.append(x)
    typeDF["Rates of Change"] = mean_plist
    typeDF = typeDF.drop(columns =["Rate of Change"])
    return typeDF

def Rate_of_Change_Project():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)

    #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    projectList = df.loc[3, :].values.tolist()
    projectList.pop(0)

    #create the dataframe   
    projectDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    projectDF["Project"] = projectList
    projectDF = projectDF.groupby(by=["Project"]).mean()
    changelist = projectDF['Rate of Change'].tolist()
    mean_plist = []
    for x in changelist:
        x = "{:.2%}".format(x)
        mean_plist.append(x)
    projectDF["Rates of Change"] = mean_plist
    projectDF = projectDF.drop(columns =["Rate of Change"])
    return projectDF

def Rate_of_Change_Affiliation():

    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)

    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)

    #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    affiliationList = df.loc[4, :].values.tolist()
    affiliationList.pop(0)

    #create the dataframe   
    affiliationDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    affiliationDF["Affiliation"] = affiliationList
    affiliationDF = affiliationDF.groupby(by=["Affiliation"]).mean()
    changelist = affiliationDF['Rate of Change'].tolist()
    mean_plist = []
    for x in changelist:
        x = "{:.2%}".format(x)
        mean_plist.append(x)
    affiliationDF["Rates of Change"] = mean_plist
    affiliationDF = affiliationDF.drop(columns =["Rate of Change"])
    return affiliationDF

def lineChart2(ProjectName):
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    list = df["Twitter Accounts"].tolist()
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)

    #filter for only primary accounts 
    sub_df = df.loc[: , (df == 'Primary Account').any()]
    #set desired header based on row position
    sub_df.columns = sub_df.iloc[3]  
    
    #drop irrelevant rows
    sub_df = sub_df.drop([0,1,2,3,4,5])
    #set index to date list 
    sub_df.index = list
    fig = px.line(sub_df, x=sub_df.index, y=sub_df[ProjectName], title='Follower Count Growth')
    # Edit the layout
    fig = fig.update_layout(title='Follower Count Growth',
                xaxis_title='Date',
                yaxis_title='Follower Count',
                template = "plotly_dark")
    return fig

def lineChart(ProjectName):
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")

    #create a date list for the x axis
    list = df["Twitter Accounts"].tolist()
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)
    list.pop(0)

    #filter for only primary accounts 
    sub_df = df.loc[: , (df == 'Primary Account').any()]
    sub_df.head(5)

    #set desired header based on row position
    sub_df.columns = sub_df.iloc[3]  
    
    #drop irrelevant rows
    sub_df = sub_df.drop([0,1,2,3,4,5])
    sub_df.head(5)

    #set index to date list 
    sub_df.index = list
    #choose desired project
    newplot = sub_df[ProjectName].plot()
    return newplot

def ProjectbySector(selection):
    #organize values into a list called datelist
    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    
    df2 = df.transpose()
    new_header = df2.iloc[0] #grab the first row for the header
    df2 = df2[1:] #take the data less the header row
    df2.columns = new_header #set the header row as the df header
    
    classifications = df.head(5)
    byTwitterHandleOBJECT = classifications.set_index('Twitter Accounts').to_dict('list')
    keysList = list(byTwitterHandleOBJECT.keys())
    DatesFollowers = df[df['RarityHomestead'].astype(str).str.isdigit()]
    Dates_dict = DatesFollowers.to_dict('list')
    datelist = list(Dates_dict.values())
    datelist.pop(0)
    
    #take the datelist values and output a new np array of the change and name it growth_rate
    growth_rate = np.exp(np.diff(np.log(datelist)))  -1
    np.set_printoptions(suppress=True)
    growth_rate.tolist()
    mean_growth_rate = []
    for x in growth_rate:
        mean = np.mean(x)
        mean_growth_rate.append(mean)
    mean_percentagelist = []
    for x in mean_growth_rate:
        x = "{:.2%}".format(x)
        mean_percentagelist.append(x)
        
 #create a dictionary to turn into a dataframe classified by twitter name with values as the new mean list
    res = {}
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            res[key] = value
            mean_growth_rate.remove(value)
            break
    for key in byTwitterHandleOBJECT:
        for value in mean_growth_rate:
            byTwitterHandleOBJECT[key].append(value)
            mean_growth_rate.remove(value)
            break
    sectorList = df.loc[0, :].values.tolist()
    sectorList.pop(0)
    
    Projectlist = df2["Project"].tolist()
    sectorProject = {Projectlist[i]: sectorList[i] for i in range(len(Projectlist))}
    s = sectorProject[selection]
    #create the dataframe   
    MeanSectorDF = pd.DataFrame.from_dict(res, orient='index', columns = ['Rate of Change'])
    MeanSectorDF["Sector"] = sectorList
    MeanSectorDF["Project"] = Projectlist
    MeanSectorDF["Rate of change %"] = mean_percentagelist 
    sectorProject = {Projectlist[i]: sectorList[i] for i in range(len(Projectlist))}
    s = str(sectorProject[selection])
    filterDF = MeanSectorDF["Sector"] == s
    SortedfilterDF = MeanSectorDF[filterDF]
    SortedfilterDF = SortedfilterDF.drop(columns = ["Rate of Change"])
    return SortedfilterDF
# growth_by_handle()
# sectorGrowth()
# SUBsectorGrowth()
# TypeGrowth()
# ProjectGrowth()
# Rate_of_Change_Sector()
# Rate_of_Change_type()
# Rate_of_Change_Project()
# Rate_of_Change_Affiliation()
# lineChart(ProjectName)
