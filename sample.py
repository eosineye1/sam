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

#Histogram for a specific column
def plotHistogram(column):
    return df[column].plot.hist()

#Sum values of a specific object
def getSumOfColumn(column):
    return df[column].sum()

#Median values of a specific object
def getMedianOfColumn(column):
    return df[column].median()

#Quartile values of a specific object
def getQuartileOfColumn(column, x, y):
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
def getMinOfColumn(column):
    return df[column].min()

#Maximum values of a specific object
def getMaxOfColumn(column):
    return df[column].max()

#Mean values of a specific object
def getMeanOfColumn(column):
    return df[column].mean()

#Variance values of a specific object
def getVarOfColumn(column):
    return df[column].var()

#Standard Deviation values of a specific object
def getStdOfColumn(column):
    return df[column].std()

#Get list of column names
def getDataColumnNames():
    return df.columns

#creates a chart
#scatter, line, bar
def plot(x_axis, y_axis, kindOfGraph):
    import matplotlib.pyplot as plt
    df.plot(x =x_axis, y=y_axis, kind =kindOfGraph)
    plt.show()

#creates a pie chart
def plotPieChart(name, width, height):
    import matplotlib.pyplot as plt
    df.plot.pie(y=name,figsize=(width, height),autopct='%1.1f%%', startangle=90)
    plt.show()
    

def botSpeak(message):
     ChatLog.config(state=NORMAL)
     ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
     ChatLog.insert(END, "Bot: " + message + '\n\n')
     ChatLog.config(state=DISABLED)
     ChatLog.yview(END)


def getInput():
    return EntryBox.get("1.0",'end-1c').strip()

def yesOrNo(response, boolAxis):
    if(boolAxis):
        if 'YES' == response.toUpper():
            return FALSE
        else:
            return TRUE
    else:
        if 'YES' == response.toUpper():
            return TRUE
        else:
            return FALSE


def getUserXAxis():
    x_axis_boolean = TRUE
    x_axis = null
    while(x_axis_boolean):
        botSpeak('What do you want to label the x-axis?')
        x_axis = getInput()
        botSpeak('\n\nThe x-axis is labeled {}. Is that correct?'.format(x_axis))
        response = getInput()
        x_axis_boolean = yesOrNo(response)
        
    return x_axis
    
def getUserYAxis():
    y_axis_boolean = TRUE
    y_axis = null
    while(y_axis_boolean):
        botSpeak('What do you want to label the y-axis?')
        y_axis = getInput()
        botSpeak('\n\nThe y-axis is labeled {}. Is that correct?'.format(y_axis))
        response = getInput()
        y_axis_boolean = yesOrNo(response) 

    return y_axis 
    
    
def graphOptions():
     
    botSpeak('I can create a scatterplot, histogram, pie, bar, and line chart.\n\nPlease confirm which chart you want or type back if you want me to do something else?')
    msg = getInput()
        
    if "scatter" in msg:
            while TRUE:
                botSpeak('You want me to create a scatterplot, is that correct?')
                response = getInput()
        
                if yesOrNo(response):
                    axis_x = getUserXAxis()
                    axis_y = getUserYAxis()
                    plot(axis_x, axis_right, 'scatter')
                else:
                    break
                 
         
         
         
def chatbot_response(msg):
    msg = msg.upper()
    print(msg)
    
    if "PLOT" in msg or "CHART" in msg or "GRAPH" in msg:
        #print("PLOT" in msg or "CHART" in msg or "GRAPH" in msg)
        graphOptions()
    #else:
        #botSpeak("I did not understand that. Could you please let me know what graoh you want?")
   


def startText(start):
    if start:
        botSpeak('Welcome to MIDAC. Which stands for Menu-Driven Interactive Data Anlysis Chat-bot\n\n I can help you analyse data.\n\nJust type how can you help me.')
 
        
      
    


#Creating GUI with tkinter
import tkinter
from tkinter import *
df = pd.read_csv("Book1.csv")
start = TRUE


def send():
    msg = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    
    

    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        chatbot_response(msg)
    
          
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
 

base = Tk()
base.title("Chatbot")
base.geometry("400x565")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="#ff3366", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=3,
                    bd=0, bg="#32de97", activebackground="#2ec4b6",fg='#1dad3a',
                    command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="#ff3366",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=540)
ChatLog.place(x=6,y=6, height=386, width=370)

EntryBox.place(x=6, y=401, height=90, width=370)
SendButton.place(x=6, y=500, width=370, height=50)

startText(start);
    
base.mainloop()





