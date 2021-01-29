#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:40:55 2021

@author: eniolaosineye
"""

import pandas as pd

def getInput():
    return input().strip()

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
def getQuantileOfColumn(column, df):
    return df[column].quartile([0.25, 0.5, 0.75, 1.0])

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
            

def runGraph(df):
    while True:
        graphOptions()
        response = getInput()
        if 'pie' in response or response == '1':        
            while True:
                print('\nWhat column do you want the pie chart to display?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                response = getInput()
                columnNames = getDataColumnNames(df)
               
                if response in columnNames:
                    try:
                        int(df[response][0])
                        print('\nHere is your pie chart:')
                        df.set_index("Name", inplace = True)
                        plotPieChart(response, 5, 5, df)
                        break                  
                    except:
                        print('\nThe column selected does not contain numbers')
                elif 'column' in response or response == '1':
                    print(columnNames)
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                else:
                    doNotUnderstand()

        elif 'scatter' in response or response == '2':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be?')
                print('(1)To see all column names, just let me know')
                print('(0) Go back')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
               
                if x_axis in columnNames:
                    while True:
                        print('\nWhat column do you want the y axis to be?')
                        print('(1) To see all column names, just let me know')
                        print('(0) Go back')
                        y_axis = getInput()

                       
                        if y_axis in columnNames :
                            print('\nHere is your scatter plot:')
                            plot(x_axis, y_axis, 'scatter', df)
                            x_axis_boolean = False
                            break
                        elif 'column' in y_axis or 'column name' in y_axis or y_axis == '1':
                            print(columnNames)
                        elif 'back' in y_axis or 'end' in y_axis or 'exit' in y_axis or 'no' in y_axis or y_axis == '0':
                            break
                        else:
                            doNotUnderstand()
                elif 'column' in x_axis or 'name' in x_axis or x_axis == '1':
                    print(columnNames)
                elif 'back' in x_axis or 'end' in x_axis or 'exit' in x_axis or 'no' in x_axis or x_axis == '0':
                    break
                else:
                    doNotUnderstand()
                   
                   
        elif 'line' in response or response == '3':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
               
                try:
                    is_int(int(df[x_axis][0]))
                    print('\nThe column selected for the x axis should not contain numbers')
                except:
                    if x_axis in columnNames:
                        while True:
                            print('\nWhat column do you want the y axis to be?')
                            print('(1) To see all column names, just let me know')
                            print('(0) Go back')
                            y_axis = getInput()
                           
                            if y_axis in columnNames:
                         
                           
                                try:
                                    int(df[y_axis][0])
                                    print('\nHere is your line chart:')
                                    plot(x_axis, y_axis, 'line', df)
                                    x_axis_boolean = False
                                    break
                                           
                                except:
                                    print('\nThe column selected for the y_axis does not contain numbers')
                           
                               
                            elif 'column' in y_axis or 'column name' in y_axis or y_axis == '1':
                                print(columnNames)
                            elif 'back' in y_axis or 'end' in y_axis or 'exit' in y_axis or 'no' in y_axis or y_axis == '0':
                                break
                            else:
                                doNotUnderstand()
                 
                    elif 'column' in x_axis or 'name' in x_axis or x_axis == '1':
                        print(columnNames)
                    elif 'back' in x_axis or 'end' in x_axis or 'exit' in x_axis or 'no' in x_axis or x_axis == '0':
                        break
                    else:
                        doNotUnderstand()
        elif 'bar' in response or response == '4':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
               
                try:
                    is_int(int(df[x_axis][0]))
                    print('\nThe column selected for the x axis should not contain numbers')
                except:
                    if x_axis in columnNames:
                        while True:
                            print('\nWhat column do you want the y axis to be? To see all column names, just let me know')
                            print('(1) To see all column names, just let me know')
                            print('(0) Go back')
                            y_axis = getInput()
   
                           
                            if y_axis in columnNames:
                                print('\nHere is your bar chart:')
                                plot(x_axis, y_axis, 'bar', df)
                                x_axis_boolean = False
                                break
                            elif 'column' in y_axis or 'column name' in y_axis or y_axis == '1':
                                print(columnNames)
                            elif 'back' in y_axis or 'end' in y_axis or 'exit' in y_axis or 'no' in y_axis or y_axis == '0':
                                break
                            else:
                                doNotUnderstand()
                    elif 'column' in x_axis or 'column name' in x_axis or x_axis == '1':
                        print(columnNames)
                    elif 'back' in y_axis or 'end' in y_axis or 'exit' in y_axis or 'no' in y_axis or y_axis == '0':
                        break
                    else:
                        doNotUnderstand()
        elif 'histogram' in response or response == '5':
             while True:
                print('\nWhat column do you want the histogram to display?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                response = getInput()
                columnNames = getDataColumnNames(df)
               
                if 'column' in response or response == '1':
                    print(columnNames)
                elif response in columnNames:
                    if type(df[response][0]) != str:
                        print('\nHere is your histogram:')
                        plotHistogram(response, df)
                        break
                    else:
                        print('\nPlease choose a column that has a numerical data type.')
                else:
                    print('\nThe column inputted does not exist in the dataframe')
        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
            break
        else:
            doNotUnderstand()


    while True:
        graphOptions()
        response = getInput()
        if 'pie' in response or response == '1':        
            while True:
                print('\nWhat column do you want the pie chart to display?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                response = getInput()
                columnNames = getDataColumnNames(df)
                
                if response in columnNames:
                    try:
                        int(df[response][0])
                        print('\nHere is your pie chart:')
                        df.set_index("Name", inplace = True)
                        plotPieChart(response, 5, 5, df)
                        break                  
                    except:
                        print('\nThe column selected does not contain numbers')
                elif 'column' in response or response == '1':
                    print(columnNames)
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                else:
                    doNotUnderstand()

        elif 'scatter' in response or response == '2':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be?')
                print('(1)To see all column names, just let me know')
                print('(0) Go back')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
                
                if x_axis in columnNames:
                    while True:
                        print('\nWhat column do you want the y axis to be?') 
                        print('(1) To see all column names, just let me know')
                        print('(0) Go back')
                        y_axis = getInput()

                        
                        if y_axis in columnNames or response == '1':
                            print('\nHere is your scatter plot:')
                            plot(x_axis, y_axis, 'scatter')
                            x_axis_boolean = False
                            break
                        elif 'column' in y_axis or 'column name' in y_axis:
                            print(columnNames)
                        elif 'back' in y_axis or 'end' in y_axis or 'exit' in y_axis or 'no' in y_axis or y_axis == '0':
                            break
                        else:
                            doNotUnderstand()
                elif 'column' in x_axis or 'name' in x_axis or x_axis == '1':
                    print(columnNames)
                elif 'back' in x_axis or 'end' in x_axis or 'exit' in x_axis or 'no' in x_axis or x_axis == '0':
                    break
                else:
                    doNotUnderstand()
        elif 'line' in response or response == '3':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be? To see all column names, just let me know')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
                if 'column' in x_axis or 'name' in x_axis:
                    print(columnNames)
                elif x_axis in columnNames:
                    while True:
                        print('\nWhat column do you want the y axis to be? To see all column names, just let me know')
                        y_axis = getInput()
                        if 'column' in y_axis or 'column name' in y_axis:
                            print(columnNames)
                        elif y_axis in columnNames:
                            print('\nHere is your line chart:')
                            plot(x_axis, y_axis, 'line')
                            x_axis_boolean = False
                            break
                        else:
                            doNotUnderstand()
                else:
                    doNotUnderstand()
        elif 'bar' in response or response == '4':
            x_axis_boolean = True
            while x_axis_boolean:
                print('\nWhat column do you want the x axis to be? To see all column names, just let me know')
                x_axis = getInput()
                columnNames = getDataColumnNames(df)
                if 'column' in x_axis or 'name' in x_axis:
                    print(columnNames)
                elif x_axis in columnNames:
                    while True:
                        print('\nWhat column do you want the y axis to be? To see all column names, just let me know')
                        y_axis = getInput()

                        if 'column' in y_axis or 'column name' in y_axis:
                            print(columnNames)
                        elif y_axis in columnNames:
                            print('\nHere is your bar chart:')
                            plot(x_axis, y_axis, 'bar')
                            x_axis_boolean = False
                            break
                        else:
                            doNotUnderstand()
                else:
                    doNotUnderstand()
        elif 'histogram' in response or response == '5':
             while True:
                print('\nWhat column do you want the histogram to display? To see all column names, just let me know')
                response = getInput()
                columnNames = getDataColumnNames()
                if 'column' in response:
                    print(columnNames)
                elif response in columnNames:
                    if type(df[response][0]) != str:
                        print('\nHere is your histogram:')
                        plotHistogram(df[response])
                        break
                    else:
                        print('\nPlease choose a column that has a numerical data type.')
                else:
                    print('\nThe column inputted does not exist in the dataframe')
        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
            break
        else:
            doNotUnderstand()
                
                
                