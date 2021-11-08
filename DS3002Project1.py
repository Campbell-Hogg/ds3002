#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 16:44:55 2021

@author: campbellhogg
"""

#I set my directory to a desktop folder on my local machine, where I stored the dataset I downloaded from Kaggle

# Install Libraries
import numpy as np
import csv 
from csv import DictWriter
import json
import pandas as pd

#ingest local csv file mounted to look at data in a pandas dataframe
happiness_data = pd.read_csv("2015.csv")

#modify file by dropping one of the columns: residual column is dropped 
#column is dropped because it doesn't give as much insight as other included data
happiness_data = happiness_data.drop(["Dystopia Residual"], axis = 1)

#export pandas dataframe to a csv file so it can be converted to a json file later
happiness_data.to_csv('happy_2015.csv', index=False)

#function to convert csv file to json
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data w/ dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'happy_2015.csv' #original csv file of world happiness report data
jsonFilePath = r'happiness_data.json' #json file wrtten to my local disk

# run function included above in script to write csv file to json
csv_to_json(csvFilePath, jsonFilePath) 

# Open JSON file
happiness_json = open('happiness_data.json',)
# returns JSON object of happiness data as a dictionary
happiness_dict = json.load(happiness_json)
print("Number of Columns:", len(happiness_dict[0])) #number of columns for each json entry
number_of_nations = len(happiness_dict) #store and print number of entries
print("Number of Records:", number_of_nations)


