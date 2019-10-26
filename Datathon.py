# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # Datathon
#%% [markdown]
# ## Question
# Is it possible to predict the number of for-hire vehicle (FHV) customers in certain areas of the city according to previews pickup data (day, time), weather and neighbourhood demographics as well as the likely destination?

#%% [markdown]
# ## Libraries
import numpy                 as np
import pandas                as pd
import matplotlib.pyplot     as plt
import seaborn               as sns
import sklearn.metrics       as Metrics
import pandas                as pd
import matplotlib.pyplot     as plt
import os
from pathlib import Path

import folium  #needed for interactive map
from folium.plugins import HeatMap

from   collections           import Counter
from   sklearn               import preprocessing
from   datetime              import datetime
from   collections           import Counter
from   math                  import exp
from   sklearn.linear_model  import LinearRegression as LinReg
from   sklearn.metrics       import mean_absolute_error
from   sklearn.metrics       import median_absolute_error
from   sklearn.metrics       import r2_score

%matplotlib inline
sns.set()
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
#%% [markdown]
# ## Collecting and Reviewing Data
#%% [markdown]
# Data are coming from files delivered by the TA's as well as data coming from NYC Open Data. To take a look at the data we are using Visual Studio Code as an IDE with its extension DataPreview in order to explore variables and information provided. But we also create some scripts in order to know some possible problems we could have with the data.

#%%
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
# print(listOfFiles)
# for file in listOfFiles:
#     print(os.path.basename(file))
#     print(Path(file).stem)

#%%
listOfDataFrames={}
for file in listOfFiles:
    listOfDataFrames[Path(file).stem]= [file,pd.read_csv(file)]

#%%

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
            self.dataFrame=pd.read_csv(self.__path)
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

listOfDataSets={}
for key,value in listOfDataFrames.items():
    listOfDataSets[key]=dataset(key,value[0],value[1])

#%% [markdown]
#For that, we first analyze the data types of datasets in order to see if there is necessary any kind of conversion and above all if the data is homogenous or if it is needed a custom transformation

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
#From above, we found that most of data types are well inferred by Pandas, but for feature work it is necessary to make some data type conversions for fields that are datetime
#So we procced on that.
for key,value in listOfDataSets.items():
    value.inferredDatetimeColumnsForConversion()
    print()
    print("Dataset " + key)
    print()
    print("-----Data Types-------")
    print(value.getColumnsDataTypes())
    print()

#%% [markdown]
#Now it's time to see if there is any null values we must deal with them

#%%
for key,value in listOfDataSets.items():
    print()
    print("Dataset " + key +" with " + str(value.getRowsCount()) + " rows")
    print()
    print(value.isNull())
    print()

#%%

# for d in listOfDataSets.values():
#     print()
#     print("-----Data Types-------")
#     print(d.getColumnsDataTypes())
#     print()

#%% [markdown]
# ## Data Cleaning

#%%


#%% [markdown]
# ## Modeling and Analyzing the Data Sets

#%%
# inferredColumns=[x for y in listOfDataSets.values() for x in y.getColumnsNames() if 'date' in x.lower()]
# inferredColumns

