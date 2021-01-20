#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:33:05 2021

@author: eniolaosineye
"""

import pandas as pd


#Select first n rows or Select last n rows
def getSample(n, head):
    if(head):
        return df.head(n)
    else:
        return df.tail(n)
    

#Randomly select n rows.
def getRandomSample(n):
    return df.sample(n)
   
## of rows in DataFrame. 
def getLength():
    return len(df)

#Select rows by position.
def selectRows(x,y):
    if(y>=x):
        return df.iloc[x:y]
    else:
        return -1
    
#Select single column with specific name
def selectSpecificColumn(name):
    return df[name]

#Select multiple columns with specific names.
def selectSpecifiColumns(names):
    return df[names]

#Select all columns between x2 and x4 (inclusive).
def selectAllColumnsBetween(x, y):
    return df.loc[:,x:y]
#Select columns in positions 1, 2 and 5 (first column is 0).
def selectAllColumnsAtLocations(locations):
    return df.iloc[:,locations]

def plotHistogram():
    return df.plot.hist()


df = pd.read_csv("Book1.csv")
print(df.head(5))

plotHistogram()

