# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 21:01:06 2021

@author: User
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:25:36 2021

@author: eniolaosineye
"""
from functions import getSample, getRandomSample, getLength, selectRows, selectSpecificColumn, selectSpecifiColumns, selectAllColumnsBetween
from functions import plotHistogram, getSumOfColumn, getMedianOfColumn, getQuartileOfColumn, getMinOfColumn, getMaxOfColumn, getMeanOfColumn 
from functions import getStdOfColumn, getDataColumnNames, plot, plotPieChart, is_int, selectAllColumnsAtLocations, getVarOfColumn
from functions import runSample, runLength, welcome, doNotUnderstand, sampleOptions, graphOptions, mainOptions, runGraph, getInput




    
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
    
        



#import pandas as pd

#df = pd.read_csv("Book1.csv")
#welcome()
import tkinter
from tkinter import *

def send():
    while True:
    response = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
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
        print(df.describe())
    
    #Go Back
    elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
        print('Exiting MIDAC. See you later!')
        break
    
    #Try again
    else:
        doNotUnderstand()
    
def botResponse(msg):
    ChatLog.config(state=NORMAL)
    
    #ChatLog.insert(END, "You: " + msg + '\n\n')
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
           
    ChatLog.insert(END, "Bot: " + msg + '\n\n')
            
    ChatLog.config(state=DISABLED)
    
    ChatLog.yview(END)    



base = Tk()
base.title("Chatbot")
base.geometry("400x565")
base.resizable(width=False, height=False)

#Create Chat window
ChatLog = Text(base, bd=0, bg="#ff3366", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=3,
                    bd=0, bg="#32de97", activebackground="#2ec4b6",fg='#1dad3a',
                    command= send)

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="#ff3366",width="29", height="5", font="Arial")
#EntryBox.bind("<Enter>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=540)
ChatLog.place(x=6,y=6, height=386, width=370)

EntryBox.place(x=6, y=401, height=90, width=370)
SendButton.place(x=6, y=500, width=370, height=50)


botResponse("Hi, My name is Midac. That stands for Menu-Driven Interactive Data Analysis Chatbot\n\n")
msg = mainOptions()
print(msg)
botResponse(msg)


base.mainloop()

    
'''while True:
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
        print(df.describe())
    
    #Go Back
    elif 'back' in response or 'end' in response or 'exit' in response or 'no' in response or response == '0':
        print('Exiting MIDAC. See you later!')
        break
    
    #Try again
    else:
        doNotUnderstand()'''
        
