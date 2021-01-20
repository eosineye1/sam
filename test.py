#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:25:36 2021

@author: eniolaosineye
"""
from functions import getSample, getRandomSample, getLength, selectRows, selectSpecificColumn, selectSpecifiColumns, selectAllColumnsBetween
from functions import plotHistogram, getSumOfColumn, getMedianOfColumn, getQuartileOfColumn, getMinOfColumn, getMaxOfColumn, getMeanOfColumn 
from functions import getStdOfColumn, getDataColumnNames, plot, plotPieChart, is_int, selectAllColumnsAtLocations, getVarOfColumn
from functions import runSample, runLength, welcome, doNotUnderstand, sampleOptions, graphOptions, mainOptions


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
                columnNames = getDataColumnNames()
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
                columnNames = getDataColumnNames()
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

    
#### THIS NEEDS TO BE FIXED

            
            
def runColumn(df):
    while True:
        print('\nI can get you a one or multiple columns.')
        print('(1) One column')
        print('(2) More than one column')
        print('(0) Go back')
        response = getInput()
        columnNames = getDataColumnNames()
        
        if 'one' in response or response == '1':
            while True:
                print('\nWhat column do you want?')
                response = getInput()
                if response in columnNames:
                    print(selectSpecificColumn(response))
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                else:
                    doNotUnderstand()
                
        elif 'multiple' in response or 'more' in response or 'two' in response or 'three' in response or response == '2':
            while True:
                print('\nYou can get multiple columns by:')
                print('(1) By name')
                print('(2) From one column to another, including all columns inbetween')
                print('(3) Columns at specific locations')
                print('(0) Go back')
                
                response = getInput()
                
                if 'name' in response or response == '1':
                    while True:
                        print('\nHow many columns do you want?')
                        response = getInput()
                        count = int(response)
                        if is_int(count):
                            listOfColumns = []
                            for x in range(count):
                                while True:
                                    print('Column name #{}'.format(x+1))
                                    response = getInput()
                                    if response in columnNames:
                                        listOfColumns.append(response)
                                        break
                                    else:
                                        print('\nThe column inputted does not exist in the dataframe')    
                                
                            print(selectSpecifiColumns(listOfColumns)) 
                            break
                          
                        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break 
                        else:
                            doNotUnderstand()
                
                elif 'inbetween' in response or 'including' in response or response == '2':
                    firstColumn = ''
                    lastColumn = ''
                    while True:
                        print('\nWhat is the first column')
                        response = getInput()
                        if response in columnNames:
                            firstColumn = response
                            break
                        else:
                            print('\nThe column inputted does not exist in the dataframe')
                    while True:
                        print('\nWhat is the second column')
                        response = getInput()
                        if response in columnNames:
                            lastColumn = response
                            break
                        else:
                            print('\nThe column inputted does not exist in the dataframe') 
                    selectAllColumnsBetween(firstColumn, lastColumn)
                    break
                    
                    
                    
                    
                elif 'specific' in response or 'location' in response or response == '3':
                    while True:
                        print('\nHow many columns do you want?')
                        response = getInput()
                        count = int(response)
                        if is_int(count):
                            listOfColumns = []
                            for x in range(count):
                                while True:
                                    print('Column name #{}'.format(x+1))
                                    response = int(getInput())
                                    if is_int(response):
                                        if x == 0:
                                            listOfColumns.append(response-1)
                                            break
                                        elif response > listOfColumns[x -1]:
                                            listOfColumns.append(response-1)
                                            break
                                        else:
                                            print('\nNumber entered must be greate than previous number entered')
                                    else:
                                        print('\nPlease enter an interger')    
                                
                            print(selectAllColumnsAtLocations(listOfColumns))
                            break
                          
                        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break 
                        else:
                            doNotUnderstand()
                    
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                else:
                    doNotUnderstand()
                    
                    
        elif response == '0':
            break
        else:
            doNotUnderstand()
    
        
def getInput():
    return input().strip()


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
        runColumn()
    
    #Option to get rows from dataframe
    elif 'row' in response or response == '6':
        print('rows')
        #runRow()
           
    #Option to describe the data in the dataframe
    elif 'describe' in response or 'descriptive' in response or 'statistic' in response or response == '7':
        print('descriptive statistics')
    
    #Go Back
    elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
        print('Exiting MIDAC. See you later!')
        break
    
    #Try again
    else:
        doNotUnderstand()