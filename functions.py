#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:40:55 2021

@author: eniolaosineye
"""

import pandas as pd

def welcome():
    print('\nHi, My name is Midac. That stands for Menu-Driven Interactive Data Analysis Chatbot')
    
def doNotUnderstand():
    print('\nI did not understand. Please choose from the options below')
    
def mainOptions():
    print('\nThese are the main things I can do for you.')
    print('(1) Clean data')
    print('(2) Get a sample of the data')
    print('(3) Get size of data')
    print('(4) Create a chart')
    print('(5) Select column(s)')
    print('(6) Select row(s)')
    print('(7) Perform Descriptive Statistics')
    print('(0) Exit MIDAC ')

def sampleOptions():
    print('\nSample options:')
    print('(1) Sample from top')
    print('(2) Sample from bottom')
    print('(3) Random sample')
    print('(0) Go back ')

def graphOptions():
    print('\nGraph options:')
    print('(1) Pie Chart')
    print('(2) Scatter Plot')
    print('(3) Line Chart')
    print('(4) Bar Chart')
    print('(5) Histogram')
    print('(0) Go Back')


#Select first n rows or Select last n rows
def getSample(n, head, df):
    if(head):
        return df.head(n)
    else:
        return df.tail(n)
    
#Randomly select n rows.
def getRandomSample(n, df):
    return df.sample(n)
   
## of rows in DataFrame. 
def getLength(name, df):
    return len(df[name])

#Select rows by position.
def selectRows(x,y, df):
    if(y>=x):
        return df.iloc[x:y]
    else:
        return -1
    
#Select single column with specific name
def selectSpecificColumn(name, df):
    return df[name]

#Select multiple columns with specific names.
def selectSpecifiColumns(names, df):
    return df[names]

#Select all columns between x2 and x4 (inclusive).
def selectAllColumnsBetween(x, y, df):
    return df.loc[:,x:y]
#Select columns in positions 1, 2 and 5 (first column is 0).
def selectAllColumnsAtLocations(locations, df):
    return df.iloc[:,locations]

#Histogram for a specific column
def plotHistogram(column, df):
    return df[column].plot.hist()

#Sum values of a specific object
def getSumOfColumn(column, df):
    return df[column].sum()

#Median values of a specific object
def getMedianOfColumn(column, df):
    return df[column].median()

#Quartile values of a specific object
def getQuartileOfColumn(column, x, y, df):
    if x > 4 or y > 4:
        return -1
    else:
        first = 0 
        last = 0
        if x == 1:
            first = 0.25
        elif x == 2:
            first = 0.5
        elif x == 3:
            first = 0.75
        else:
            first = 1
        
        if y == 1:
            last = 0.25
        elif y == 2:
            last = 0.5
        elif y == 3:
            last = 0.75
        else:
            last = 1
            
        return df[column].quartile([first,last])

#Minimum values of a specific object
def getMinOfColumn(column, df):
    return df[column].min()

#Maximum values of a specific object
def getMaxOfColumn(column, df):
    return df[column].max()

#Mean values of a specific object
def getMeanOfColumn(column, df):
    return df[column].mean()

#Variance values of a specific object
def getVarOfColumn(column, df):
    return df[column].var()

#Standard Deviation values of a specific object
def getStdOfColumn(column, df):
    return df[column].std()

#Get list of column names
def getDataColumnNames(df):
    return df.columns


#creates a chart
#scatter, line, bar
def plot(x_axis, y_axis, kindOfGraph, df):
    import matplotlib.pyplot as plt
    df.plot(x =x_axis, y=y_axis, kind =kindOfGraph)
    plt.show()

#creates a pie chart
def plotPieChart(name, width, height, df):
    import matplotlib.pyplot as plt
    df.plot.pie(y=name,figsize=(width, height),autopct='%1.1f%%', startangle=90)
    plt.show()

    
def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

def runSample(df):
    while True:
        
        print('\nWhat is the sample size that you want? \n\n(0)Or go back?')
        response = getInput()
      
            
        if 'back' in response or response == '0':
            break
        else:
            try:
                sampleSize = int(response)
                if is_int(sampleSize) and sampleSize > 1:
                    while True:
                        sampleOptions()
                        response = getInput()
                        if 'top' in response or response == '1':
                            print(getSample(sampleSize, True, df))
                            break
                        elif 'bottom' in response or response == '2':
                            print(getSample(sampleSize, False, df))
                            break
                        elif 'random' in response or response == '3':
                            print(getRandomSample(sampleSize, df))
                            break
                        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break
                        else:
                            doNotUnderstand()
                else:
                    print('\nPlease eneter a number greater than 0')
      
            except:
                print('\nPlease enter a valid integer')
                
                
                
def runLength(df):
    while True:
        print('(1) Do you want the size of the whole dataframe?\n(2) Or a specific column? \n(3) To see all column names, just let me know.\n(0) Go back')
        response = getInput()
        columnNames = getDataColumnNames(df)
            
        if 'all' in response or 'whole' in response or response == '1':
            print('The length of the whole dataframe is {}'.format(len(df)))
           
        elif 'specific' in response or 'one' in response or response == '2':
            while True:
                print('What column do you want to see the length for? \n\n(1) Or get column names\n(0) Go back')
                response = getInput()
                
                if response in columnNames:
                    print(getLength(response, df))
                    break
                elif 'column' in response or response == '1':
                    print(columnNames)
                
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                elif response not in columnNames:
                    print('\nThe column inputted does not exist in the dataframe')  
        elif 'column' in response or response == '3':
            print(columnNames)
        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
            break
        else:
            doNotUnderstand()          
                
                
                