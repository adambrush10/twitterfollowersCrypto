import requests
import json
import pandas as pd
import os
import datetime
import csv
from datetime import datetime
import streamlit as st


def PullProject_info():

    df = pd.read_excel (r"C:\Users\adam1\___-Projects____\TwitterFollower_Project\TwitterFollowProject_pulledtoPANDAS.xlsx",sheet_name="FollowerCount")
    sub_df = df.loc[: , (df == 'Primary Account').any()]
    project = sub_df.loc[3, :].values.tolist()
    
    #load bearer token
    os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAPo1agEAAAAAdyZRW5mArn%2FUtcmFB3f9aPQWHAA%3DwiEflCIFCZyAfMsuoAJXGAf7MKmgFnAbcT3LszmGAYij8VHQYn'
    bearer_token = os.getenv('TOKEN')
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    

    namelist = []
    list1 = []

    for x in sub_df.columns:
        namelist.append(x)
        
    for x in namelist:
        username = x
        search_url = f"https://api.twitter.com/2/users/by?usernames={username}&user.fields=public_metrics,url,profile_image_url,created_at,description"
        response = requests.request("GET", search_url, headers = headers)
        json_response = response.json()
        m = response.status_code
        print(f"| Endpoint Response Code: {m}     |")
        list1.append(json_response)    
    
    size = len(list1)
    print(size)
    list2 = []
    counter = 0
    while counter < size:
        itemlist = []
        name = list1[counter]["data"][0]["username"]
        itemlist.append(name)
        web = list1[counter]["data"][0]["url"]
        itemlist.append(web)
        description = list1[counter]["data"][0]["description"]
        itemlist.append(description)
        datecreated = list1[counter]["data"][0]["created_at"]
        itemlist.append(datecreated)
        followers = list1[counter]["data"][0]["public_metrics"]["followers_count"]
        itemlist.append(followers)
        profile_image = list1[counter]["data"][0]["profile_image_url"]
        itemlist.append(profile_image)
        list2.append(itemlist)
        counter = counter +1
    finaldf = pd.DataFrame(list2,columns = ["name", "website","description","date created", "follower Count", "profile image"] )   
    finaldf["Project"] = project
    finaldf = finaldf.set_index("Project")
    return finaldf

# def coinwatchAPI():



    #PullProject_info()