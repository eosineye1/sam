#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:25:36 2021

@author: eniolaosineye
"""
from functions import getSample, getRandomSample, getLength, selectRows, selectSpecificColumn, selectSpecifiColumns, selectAllColumnsBetween
from functions import plotHistogram, getSumOfColumn, getMedianOfColumn, getQuantileOfColumn, getMinOfColumn, getMaxOfColumn, getMeanOfColumn 
from functions import getStdOfColumn, getDataColumnNames, plot, plotPieChart, is_int, selectAllColumnsAtLocations, getVarOfColumn
from functions import runSample, runLength, welcome, doNotUnderstand, sampleOptions, graphOptions, mainOptions, runGraph, getInput




    
#### THIS NEEDS TO BE FIXED

def runDescribe(df):
    while True:
        print('\nWhat column do you want to describe')
        print('(1) To see all column names, just let me know')
        print('(0) Go back')
        column = getInput()
        columnNames = getDataColumnNames(df)
        
        if column == '1'or 'column' in column or 'all' in column:
            print(columnNames)
        
        elif column in columnNames:
            
            while True:
                print('\nI can do the following things:')
                print('(1) Sum of {}'.format(column))
                print('(2) Median of {}'.format(column))
                print('(3) Quartile of {}'.format(column))
                print('(4) Minimum of {}'.format(column))
                print('(5) Maximum of {}'.format(column))
                print('(6) Mean of {}'.format(column))
                print('(7) Variance of {}'.format(column))
                print('(8) Standard deviation of {}'.format(column))
                print('(0) Go back')
            
                response = getInput()
                
                if response == '1' or 'sum' in response:
                    print("\nThe sum of {} is {}".format(column, round(getSumOfColumn(column, df))))
                    
                elif response == '2' or 'median' in response:
                    print("\nThe median of {} is {}".format(column, round(getMedianOfColumn(column, df))))
                    
                elif response == '3' or 'quartile' in response:    
                    print("\nThe quartiles of {} are {}".format(column, round(getQuantileOfColumn(column, df))))
                    
                elif response == '4' or 'minimum' in response:
                    print("\nThe min of {} is {}".format(column, round(getMinOfColumn(column, df))))
                    
                elif response == '5' or 'maximum' in response:
                    print("\nThe maximum of {} is {}".format(column, round(getMaxOfColumn(column,df))))
                    
                elif response == '6' or 'mean' in response:
                    print("\nThe mean of {} is {}".format(column, round(getMeanOfColumn(column, df))))
                    
                elif response == '7' or 'var' in response:
                    print("\nThe variance of {} is {}".format(column, round(getVarOfColumn(column,df))))
                    
                elif response == '8' or 'standard' in response or 'deviation' in response:
                    print("\nThe standard deviation of {} is {}".format(column, round(getStdOfColumn(column, df))))
                    
                elif 'back' in column or 'end' in column or 'exit' in column or 'no' in column or column == '0':
                    break
                else:
                    doNotUnderstand()
        elif 'back' in column or 'end' in column or 'exit' in column or 'no' in column or column == '0':
                    break
        else: 
            doNotUnderstand()
                
                
            
            
            
    
            
def runColumn(df):
    while True:
        print('\nI can get you a one or multiple columns.')
        print('(1) One column')
        print('(2) More than one column')
        print('(0) Go back')
        response = getInput()
        columnNames = getDataColumnNames(df)
        
        if 'one' in response or response == '1':
            while True:
                print('\nWhat column do you want?')
                print('(1) To see all column names, just let me know')
                print('(0) Go back')
                response = getInput()
                if response in columnNames:
                    print(selectSpecificColumn(response, df))
                elif 'column' in response or response == '1':
                    print(columnNames)
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
                        print('(0) Go back')
                        response = getInput()
                        
                        if 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break
                        else:
                            try:
                                count = int(response)
                                if is_int(count):
                                    listOfColumns = []
                                    for x in range(count):
                                        while True:
                                            print('\nColumn name #{}'.format(x+1))
                                            print('(1) To see all column names, just let me know')
                                            print('(0) Go back')
                                            response = getInput()
                                            if 'column' in response or response == '1':
                                                print(columnNames)
                                            elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                                                break
                                            elif response in columnNames:
                                                listOfColumns.append(response)
                                                break
                                            else:
                                                print('\nThe column inputted does not exist in the dataframe')    
                                                
                                        if 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                                            break
                                        elif len(listOfColumns) == count:
                                            print(selectSpecifiColumns(listOfColumns, df) )
                                            break
                            except:
                                print('\nNot an integer, please enter an integer')
                            
                
                elif 'inbetween' in response or 'including' in response or response == '2':
                    firstColumn = ''
                    lastColumn = ''
                    while True:
                        print('\nWhat is the first column')
                        print('(1) To see all column names, just let me know')
                        print('(0) Go back')
                        response = getInput()
                        if response in columnNames:
                            firstColumn = response
                            
                            while True:
                                print('\nWhat is the last column')
                                print('(1) To see all column names, just let me know')
                                print('(0) Go back')
                                response = getInput()
                                if response in columnNames:
                                    lastColumn = response
                                    if firstColumn != '' and lastColumn != '':
                                        print(selectAllColumnsBetween(firstColumn, lastColumn, df))
                                        break
                                        
                                    else:
                                        print('\nError getting columns, please try again.')
                                        break
                                    break
                                elif 'column' in response or response == '1':
                                    print(columnNames)
                                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                                    break
                                else:
                                    print('\nThe column inputted does not exist in the dataframe') 
                            if firstColumn != '' and lastColumn != '':
                                break
                        elif 'column' in response or response == '1':
                            print(columnNames)
                        elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break
                        else:
                            print('\nThe column inputted does not exist in the dataframe')
                 
                elif 'specific' in response or 'location' in response or response == '3':
                    while True:
                        print('\nHow many columns do you want?')
                        print('(0) Go back')
                        response = getInput()
                        
                        if 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                            break
                        
                        else:
                            try:
                                count = int(response)
                       
                                if is_int(count):
                                    listOfColumns = []
                                    for x in range(count):
                                        while True:
                                            print('\nColumn #{} at location:'.format(x+1))
                                            print('(1) To see all column names, just let me know')
                                            try:
                                                response = int(getInput())
                                                if is_int(response) and response <= len(df):
                                                    if x == 0:
                                                        listOfColumns.append(response-1)
                                                        break
                                                    elif response > listOfColumns[x -1]:
                                                        listOfColumns.append(response-1)
                                                        break
                                                    else:
                                                        print('\nNumber entered must be greate than previous number entered')
                                                elif response > len(df): 
                                                    print('\nLocation must be less than {}'.format(len(df) + 1))
                                            except:
                                                print('\nPlease enter an interger')    
                                        
                                    if len(listOfColumns) == count:
                                        print(selectAllColumnsAtLocations(listOfColumns, df))
                                        break
                                  
                                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                                    break 
                                else:
                                    doNotUnderstand()
                            except:
                                print('\nNot an integer, please enter an integer')
                elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
                    break
                else:
                    doNotUnderstand()
                    
                    
        elif response == '0':
            break
        else:
            doNotUnderstand()
    
        



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
        #print('rows')
        #runRow()
        print(df['Assist'].sum())
           
    #Option to describe the data in the dataframe
    elif 'describe' in response or 'descriptive' in response or 'statistic' in response or response == '7':
        #print('descriptive statistics')
        runDescribe(df)
        #print(df['Assist'].quantile([0.0,0.25, 0.75,1]))
    
    #Go Back
    elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
        print('Exiting MIDAC. See you later!')
        break
    
    #Try again
    else:
        doNotUnderstand()