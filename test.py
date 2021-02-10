#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:25:36 2021

@author: eniolaosineye
"""


# web transaction objects
#from bottle import request, response

# HTML request types
from bottle import route, get, put, post, delete

# web page template processor
from bottle import template

# development server
from bottle import run 

@route('/')
@route('/tasks')
def tasks():
    return template("tasks.tpl") 


if __name__ == "__main__":

    run(host='localhost', port=8080, debug=True)

'''from functions import getSample, getRandomSample, getLength, selectRows, selectSpecificColumn, selectSpecifiColumns, selectAllColumnsBetween
from functions import plotHistogram, getSumOfColumn, getMedianOfColumn, getQuantileOfColumn, getMinOfColumn, getMaxOfColumn, getMeanOfColumn 
from functions import getStdOfColumn, getDataColumnNames, plot, plotPieChart, is_int, selectAllColumnsAtLocations, getVarOfColumn
from functions import runSample, runLength, welcome, doNotUnderstand, sampleOptions, graphOptions, mainOptions, runGraph, getInput
from functions import runDescribe, runColumn


import pandas as pd

df = pd.read_csv("Book1.csv")
welcome()
    
while True:
    mainOptions()
    response = getInput()
        
    #Options to get a sample of the data
    
    #Option to clean data
    if 'clean' in response or response == '1':
        print('Clean data')
    
    #Option to get a sample of data
    elif 'sample' in response or response == '2':
        runSample(df)
             
    #Option to get length of datafram and/or column(s)
    elif 'length' in response or response == '3':
        runLength(df)
    
    #Options to create a chart from the data
    elif 'chart' in response or 'plot' in response or 'graph' in response or response == '4':
        runGraph(df)
    
    #Option to get column(s) from dataframe
    elif 'column' in response or response == '5':
        runColumn(df)
    
    #Option to get rows from dataframe
    elif 'row' in response or response == '6':
        print(selectRows(10,12, df))
           
    #Option to describe the data in the dataframe
    elif 'describe' in response or 'descriptive' in response or 'statistic' in response or response == '7':
        runDescribe(df)
    
    #Go Back
    elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
        print('Exiting MIDAC. See you later!')
        break
    
    #Try again
    else:
        doNotUnderstand()'''