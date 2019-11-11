# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%% [markdown]
# # Datathon
#%% [markdown]
# ## Question
# Is it possible to predict the number of for-hire vehicle (FHV) customers in certain areas of the city according to previews pickup data (day, time), weather and neighbourhood demographics as well as the likely destination?

#%% [markdown]
# ## Note
# We received some data that will be first analyzed and cleaned. For that, we created a semi automatic process. You only need to put your csv files in a folder called DataD.
# Then you just run this .py file or run all cells of the ipynb

#%% [markdown]
# ## Libraries
# For current and future work, we import common known libraries such as pandas, numpy, matplotlib, seaborn, folium, geopy, shapely, concurrent futures, tqdm, among others.

#%%
import cython

print("Starting to load modules ...")
import numpy                 as np
import pandas                as pd
import matplotlib.pyplot     as plt
import seaborn               as sns
import sklearn.metrics       as Metrics
import matplotlib.pyplot     as plt
import os
from pathlib import Path

import folium  #needed for interactive map
from folium.plugins import HeatMap

# To see if a point belongs to a polygon
# it is used to identified to which nta belongs a point
from shapely.geometry import Point, Polygon

# To calculate distances
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from   collections           import Counter
from   sklearn               import preprocessing
from   datetime              import datetime
from   collections           import Counter
from   math                  import exp
from   sklearn.linear_model  import LinearRegression as LinReg
from   sklearn.metrics       import mean_absolute_error
from   sklearn.metrics       import median_absolute_error
from   sklearn.metrics       import r2_score


import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor, as_completed
from multiprocessing import freeze_support, cpu_count
from tqdm.auto import tqdm
from p_tqdm import p_map
from tqdm import tqdm_notebook, tnrange,tqdm


#%matplotlib inline

sns.set()

#%% [markdown]
# ## Collecting and Reviewing Data

# As declared before, data is coming from files delivered by the TA's as well as data coming from NYC Open Data. To visualize data we are using Visual Studio Code as an IDE with its extension DataPreview in order to explore variables and information provided. But we also create some scripts in order to know some possible problems we could have with the data.
# Files such as .py, ipynb are in a folder called DS4A. Inside this folder must be the folder DataD where the csv files are located. The script will be identifying the files located there and they will be loaded automatically and async.
#%%

''' 
# Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
'''
try:
	os.chdir(os.path.join(os.getcwd(), 'DS4A'))
	#print(os.getcwd())
except:
	pass

'''
    For the given path, get the List of all files in the directory and subdirectory (I havent test that)
'''

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = []
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles= allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles 

listOfFiles = getListOfFiles('DataD')

listOfDataFrames={}

print("Starting to load files ...")

with ThreadPoolExecutor(max_workers=2) as executor:
    futures ={executor.submit(pd.read_csv,file,low_memory=False):file for file in listOfFiles}
    with tqdm(total=len(listOfFiles)) as pbar:
        for future in concurrent.futures.as_completed(futures):
            myFile=futures[future]
            pbar.update(1)
            print(myFile + " loaded")
            listOfDataFrames[Path(myFile).stem] = [myFile,future.result()]
            
#%% [markdown]
# **To keep dataFrames and general information about them we create a class that represent each dataset**
#%%

# A class that represents each file loaded.

''' -----------Class Definition ---------------- '''
class dataset:
    def __init__(self, name, path, dataFrame=None):
        self.name=name
        self.__isLoaded=False
        if dataFrame is None:
            self.loadData(path)
        else:
            self.dataFrame=dataFrame
            self.__isLoaded=True

        self.columnsDescription={}
        self.__isUpdated=False        
        self.path=path
    
    def getRowsCount(self):
        if self.__isLoaded:
            return len(self.dataFrame)
        else:
            print("There is no dataFrame loaded")
    
    def loadData(self):
        try:
            self.dataFrame=pd.read_csv(self.path)
            self.__isLoaded=True
        except:
            self.__isLoaded=False
            print("Attribute path may be empty or file doesn't exist")
            pass
    
    def updateInfo(self):
        #Implementation is missing
        self.__isUpdated=True

    def isUpdate(self):
        return self.__isUpdated
    
    def getColumnsNames(self):
        if self.__isLoaded:
            return list(self.dataFrame.columns.values)
        else:
            print("There is no dataFrame loaded")
    
    def getColumnsDataTypes(self):
        if self.__isLoaded:
            return self.dataFrame.dtypes
        else:
            print("There is no dataFrame loaded")   

    def getColumnsInfo(self):
        if self.__isLoaded:
            return self.dataFrame.info()
        else:
            print("There is no dataFrame loaded")  

    def getDataFrameStatistics(self):
        if self.__isLoaded:
            return self.dataFrame.describe()
        else:
            print("There is no dataFrame loaded")

    #Try to infer which columns require to be converted to datetime

    def inferredDatetimeColumnsForConversion(self):
        if self.__isLoaded:
            inferredColumns=[x for x in self.getColumnsNames() if 'date' in x.lower()]
            for i in inferredColumns:
                self.dataFrame[i]=pd.to_datetime(self.dataFrame[i])
        else:
            print("There is no dataFrame loaded")

    def isNull(self):
        if self.__isLoaded:
            return self.dataFrame.isnull().sum()
        else:
            print("There is no dataFrame loaded")

''' -----------End class Definition ------------'''

#%%

#Creating a dictionary of datasets. You can access a specific dataset (dataframe or file content) through its key
print("Creating a dictionary of datasets. You can access a specific dataset (dataframe or file content) through its key")
listOfDataSets={}
for key,value in listOfDataFrames.items():
    listOfDataSets[key]=dataset(key,value[0],value[1])

#%% [markdown]
# Once loading process is done, next step is to review and extract useful information of the Data.
# 
# For that, we first analyze the data types of datasets in order to see if there is necessary any kind of conversion and above all if the data is homogenous or if a custom transformation is needed

#%%

#Code to see datasets columns types
for key,value in listOfDataSets.items():
    print()
    print("Dataset " + key +" with " + str(value.getRowsCount()) + " rows")
    print()
    print("-----Data Types-------")
    print(value.getColumnsDataTypes())
    print()

#%% [markdown]
# **Now it's time to see if there is any null values we must deal with them.**

#%%
print("Starting review process of null values")
for key,value in listOfDataSets.items():
    print()
    print("Dataset " + key +" with " + str(value.getRowsCount()) + " rows")
    print()
    print(value.isNull())
    print()


#%% [markdown]
# ## Data Cleaning
#From the above, we realize that geographics dataframe has many null values. That is because there are nta's bigger than others
#
#We decide to not use that table but create a dictionary instead, with nta as keys and list of tuples with latitude and longitude as values
#
# Next we can see a preview of 2 elements of the dictionary.
#%%

print("Creating dictionary of ntas and their surrounding coordinates")
ntas={}
geographic=listOfDataSets['geographic']
points=[]
for i in geographic.getColumnsNames():
    for j  in range(0,geographic.dataFrame[i].count()):
        if j%2 == 0:
            points.append((geographic.dataFrame.loc[j,i],geographic.dataFrame.loc[j+1,i]))
        else:
            continue
    ntas[i]=points
    points=[]
    
#ntas
from itertools import islice
n = 2
list(islice(ntas.items(),n))

#%% [markdown]
# **Important**
# For our objective, we need to know nta's of green trips, uber trips 2014 and yellow trips where we have information about latitude and longitude of the pickup and dropoff.
# 
# For uber trips 2015 we do not have that kind of information, so we removed that dataset and create a cpu intensive algorithm to find the respectively nta to the dataSets Green, Uber2014 and Yellow Trips. 
# Also, mta_trips is deleted because for our first version we are not planning to use that data.
# 
# Next you can find a code to find nta's according to lattitude and longitude info
# ```
# :::python
# def settingNta(latitude, longitude):
#     for key, value in ntas.items():
#         p1=Point(longitude,latitude)
#         poly=Polygon(value)
#         if poly.contains(p1):
#             return key
#     return "N/A"

# green=listOfDataSets['green_trips'].dataFrame
# for i in tnrange(len(green), desc = "Iterating"):
#     green["nta"]= settingNta(green["pickup_latitude"][i],green["pickup_longitude"][i])
# ```
# %%

print("deleting dataset uber_trips_2015")
if "uber_trips_2015" in listOfDataSets:
    del listOfDataSets["uber_trips_2015"]

print("deleting dataset mta_trips")
if "mta_trips" in listOfDataSets:
    del listOfDataSets["mta_trips"]


#%%

# this code is commented because is highly intensive. This process is done only once. Files are located in a folder named Definitive

# def settingNta(latitude, longitude):
#     for key, value in ntas.items():
#         p1=Point(longitude,latitude)
#         poly=Polygon(value)
#         if poly.contains(p1):
#             return key
#     return "N/A"

# green=listOfDataSets['green_trips'].dataFrame
# for i in tnrange(len(green), desc = "Iterating"):
#     green["nta"]= settingNta(green["pickup_latitude"][i],green["pickup_longitude"][i])

# green.info()

#%% [markdown]
# **Important**
# We commented the code to search for nta's due to this high intensive process may run only once. 

# Next, we saved the result of the process as a new csv files containing the nta info. So, in a folder called Definitive it's located the updated version of green_trips, uber_trips and yellow_trips

# Now, we must update our datasets respectively. A preview info about them is found below.

#%%
print("Updating datasets with nta info ...")
listOfDataSets["uber_trips_2014"].path=r"Definitive\uber_trips_2014.csv"
listOfDataSets["yellow_trips"].path=r"Definitive\yellow_trips.csv"
listOfDataSets["green_trips"].path=r"Definitive\green_trips.csv"
listOfDataSets["uber_trips_2014"].loadData()
listOfDataSets["yellow_trips"].loadData()
listOfDataSets["green_trips"].loadData()

listOfDataSets["uber_trips_2014"].dataFrame.head()
listOfDataSets["yellow_trips"].dataFrame.head()
listOfDataSets["green_trips"].dataFrame.head()

#%% [markdown]
# Also, we found that most of data types are well inferred by Pandas, but for future work it is necessary to make some data type conversions for datetime fields
#
#  **So we procced on that.**

#%%
print("Starting to infer date types in each dataFrame ...")

with ThreadPoolExecutor(max_workers=2) as executor:
    futures ={executor.submit(value.inferredDatetimeColumnsForConversion):[key,value] for key,value in listOfDataSets.items()}
    with tqdm(total=len(listOfDataSets)) as pbar:
        for future in concurrent.futures.as_completed(futures):
            key=futures[future][0]
            value=futures[future][1]
            pbar.update(1)
            print()
            print("Dataset " + key)
            print()
            print("-----Data Types-------")
            print(value.getColumnsDataTypes())
            print()
           
print("---- Inferring date type process ended ----")
print()
#%% [markdown]
# It is time to analyze information about locations in maps. For that we are analyzing green_trips

# For instance, this first mapshows in blue the pickup point in blue and the dropoff in red and a green line joining this 2 points. This shpow us that green trips can not pick up passengers in Manhattan and also help us spot outliers as is the case of a service that started in Brooklin and ended in Madagascar.
   
# **Important**
# Lines drawn are only the first 200 records of green_trips
#%%
folium_map = folium.Map(location=[40.738, -73.98],
                        zoom_start=10,
                        tiles="OpenStreetMap")

green=listOfDataSets['green_trips'].dataFrame

for i in range(0,200):
    p1=[green["pickup_latitude"][i],green["pickup_longitude"][i]]
    p2=[green["dropoff_latitude"][i],green["dropoff_longitude"][i]]
    points1=[p1,p2]

    marker = folium.CircleMarker(location=[p1[0],p1[1]],radius=5,color="blue",fill=True)
    marker.add_to(folium_map)

    marker2 = folium.CircleMarker(location=[p2[0],p2[1]],radius=5,color="red",fill=True)
    marker2.add_to(folium_map)
    
    folium.PolyLine(points1, color="green", weight=2.5, opacity=1).add_to(folium_map)

folium_map
#%% [markdown]
# A second map, This map shows us the drop off points with the highest fares. We can see that the distribution is even as it usually dependes on the lenght of the trip instead of only the dropoff point. Despite this, we were able to find that airports usually have more expensive trips.
# **Important**
# Notice that we are only plotting 100 thousand records for issues in the performance
#%%
max_amount = float(green['total_amount'].max())

folium_hmap = folium.Map(location=[40.738, -73.98],
                        zoom_start=13,
                        tiles="OpenStreetMap")
                        
green=green.head(100000)

hm_wide = HeatMap( list(zip(green["dropoff_latitude"], green["dropoff_longitude"], green['total_amount'])),
                   min_opacity=0.2,
                   max_val=max_amount,
                   radius=8, blur=6, 
                   max_zoom=15, 
                 )


folium_hmap.add_child(hm_wide)
#%% [markdown]
# ## Modeling and Analyzing the Data Sets
# In progress ...