#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:40:55 2021

@author: eniolaosineye
"""
import streamlit as st
    
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
    import matplotlib.pyplot as plt
    df[column].plot.hist()
    plt.show()

#Sum values of a specific object

def getSumOfColumn(column, df):
    return df[column].sum()

#Median values of a specific object
def getMedianOfColumn(column, df):
    return df[column].median()

#Quartile values of a specific object
def getQuantileOfColumn(column, df):
    return df[column].quantile([0.25, 0.5, 0.75, 1.0])

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

    
def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False
          
def displayStatistics(func, column, trigger, df):
    try:
        st.write('The ', trigger, ' of ', column, ' is: ', func(column, df))
            
    except:
        st.warning('The column you choice does not exist in the dataframe')
            
def displayColumns(listOfColumnNames, st, df):
    count = 1
    st.sidebar.markdown('These are the column names in the dataframe')
    for name in listOfColumnNames:
         try:
             int(df[name][0])
             st.sidebar.write(count,') ', name)
             count += 1
         except:
             pass
    

def plotGraph(func, column, st, df):
    try:
        func(df[column])
       
    except:
        st.warning('The column you choice does not exist in the dataframe')
        

def displayImageAndTitle(st):
    from PIL import Image
    logo = Image.open('assets/logo/logo.png')
    st.image(logo ,width=200)   
    st.title("MIDAC")
    st.sidebar.title("MIDAC")
    st.sidebar.markdown("Please click on an options below:")
        

def welcomeText(st):
    st.header('Hello, *World!* :sunglasses:')
    st.subheader("I'm MIDAC. I am here to help you analyze data quickly and derive information to aid in small business descisions.")
    st.subheader("To get started, just select *start* from the selecbox is the side bar on the left.")
    st.subheader("Have *fun,* \nEniola Osineye :smile:") 

def describeData(st, df, listOfColumnNames):
    
    import pandas as pd
    select = st.sidebar.selectbox('Select an option', ['Sum', 'Quartile','Median', 'Lowest', 'Highest', 'Mean', 'Variance', 'Standard Deviation', 'Comprehensive'])   
    
    
    options = []
    for name in listOfColumnNames:
       
        try: 
            int(df[name][0])
            options.append(name)
        except:
            pass
    
    if select == 'Sum':
        columnNames = st.sidebar.selectbox('Column Names', options)
        
        displayStatistics(getSumOfColumn, columnNames, 'sum', df)
        
    elif select == 'Quartile':
        columnNames = st.sidebar.selectbox('Column Names', options)
        st.write('The quartiles of ', columnNames, ' is:')
        s = getQuantileOfColumn(columnNames, df)
        s.index = ['1st', '2nd', '3rd', '4th']
        st.write(s)
        
    elif select == 'Median':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMedianOfColumn, columnNames, 'median', df)
            
    elif select == 'Lowest':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMinOfColumn, columnNames, 'lowest', df)
        select2 = st.sidebar.selectbox('Show record(s)', ['No', 'Yes',])  
        
        if select2 == 'Yes':
            size = st.number_input('Enter the sample size', min_value=1, step=1, max_value=len(df))
            smallest = df[columnNames].nsmallest(size)
            
            select3 = st.sidebar.selectbox('Minimal or Whole', ['Minimal', 'Whole'])
            
            if select3 == 'Minimal':
                st.write('The lowest records by ', columnNames, ' are: ', smallest)
            
            elif select3 == 'Whole':
                frames = []
                for row in smallest:
                    frames.append(df.loc[df[columnNames] == row])
                
                result = pd.concat(frames)
                st.write('The lowest records by ', columnNames, ' are: ')
                st.dataframe(result)
                  
    
    elif select == 'Highest':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMaxOfColumn, columnNames, 'highest', df)
        select2 = st.sidebar.selectbox('Show records', ['No', 'Yes',])  
      
        if select2 == 'Yes':
            size = st.number_input('Enter the sample size', min_value=1, step=1, max_value=len(df))
            largest = df[columnNames].nlargest(size)
            
            select3 = st.sidebar.selectbox('Minimal or Whole', ['Minimal', 'Whole'])
            
            if select3 == 'Minimal':
                st.write('The highest records by ', columnNames, ' are: ', largest)
            
            elif select3 == 'Whole':
                frames = []
                for row in largest:
                    frames.append(df.loc[df[columnNames] == row])
                
                result = pd.concat(frames)
                st.write('The highest records by ', columnNames, ' are: ')
                st.dataframe(result)
        
    
    elif select == 'Mean':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMeanOfColumn, columnNames, 'mean', df)

    elif select == 'Variance':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getVarOfColumn, columnNames,  'variance', df)
        
    elif select == 'Standard Deviation':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getStdOfColumn, columnNames, 'standard deviation', df)

    elif select == 'Comprehensive':
        columnNames = st.sidebar.selectbox('Column Names', options)
        st.write(df[columnNames].describe())
                  
   
    
def lengthOption(st, listOfColumnNames, df):
    options = ['All (length for all columns)']
    
    for name in listOfColumnNames:
        options.append(name)
    
    columnNames = st.sidebar.selectbox('Column Names', options)

    if columnNames == 'All (length for all columns)':
        st.write('The length of the whole dataframe is: ', len(df))
    else:
        st.write('The length of column ', columnNames, ' in the dataframe is: ', getLength(columnNames, df))

def graphOption(st, listOfColumnNames, df, indexColumn):
    import altair as alt
    select = st.sidebar.selectbox('Pick a graph', ['Area Chart', 'Line Chart', 'Bar Chart', 'Scatter Plot'])
 
    options = []
    for name in listOfColumnNames:
        try: 
            int(df[name][0])
            options.append(name)
        except:
            pass
    
    if select == 'Area Chart':
        select2 = st.sidebar.selectbox('Customize Bar Chart', ['No', 'Yes'])

        if select2 == 'Yes':
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index

            x_axis = st.sidebar.selectbox('X Axis', listOfColumnNames)
            y_axis = st.sidebar.selectbox('Y Axis', listOfColumnNames)

            tooltips =st.sidebar.multiselect('Tooltips (select more than one', listOfColumnNames)

            title = st.text_input('Chart Title')
            width = st.number_input('Width', step=10, min_value=200, max_value=1000)
            height = st.number_input('Height', step=10, min_value=400, max_value=1000)
            lineColor = st.sidebar.color_picker('Line color', value='#923E94')
            gradientColor = st.sidebar.color_picker('Gradient color', value='#923E94')
            c = alt.Chart(new_df).mark_area(
                    line={'color':lineColor},
                    color=alt.Gradient(
                        gradient='linear',
                        stops=[alt.GradientStop(color='white', offset=0),
                            alt.GradientStop(color=gradientColor, offset=1)],
                        x1=1,
                        x2=1,
                        y1=1,
                        y2=0
                    )
                ).encode(
                    alt.X(x_axis),
                    alt.Y(y_axis)
                ).properties(
                    title=title,
                    width=width,
                    height=height
                )
            st.write('')
            st.write('Chart:')
            st.altair_chart(c, use_container_width=True)
        else:
            columnNames = st.sidebar.selectbox('Column Names', options)
            st.write('Select the column you want the area chart to display')
            st.write('')
            st.write('Chart:')
            plotGraph(st.area_chart, columnNames, st, df)
        
    elif select == 'Line Chart':
        select2 = st.sidebar.selectbox('Customize Bar Chart', ['No', 'Yes'])

        size = st.sidebar.number_input('Sample size', step=1, min_value=1, max_value=len(df))

        if select2 == 'Yes':
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index

            x_axis = st.sidebar.selectbox('X Axis', listOfColumnNames)
            y_axis = st.sidebar.selectbox('Y Axis', listOfColumnNames)
            tooltips = st.sidebar.multiselect('Tooltips (select more than one', listOfColumnNames)
            
            title = st.text_input('Chart Title')
            
            width = st.number_input('Width', step=10, min_value=200, max_value=1000)
            height = st.number_input('Height', step=10, min_value=400, max_value=1000)
            
            c = alt.Chart(new_df[0:size]).mark_line(point=True).encode(
                x=x_axis,
                y=y_axis, 
                tooltip= tooltips).properties(
                    title=title,
                    width=width,
                    height=height)
            st.write('')
            st.write('Chart:')
            st.altair_chart(c, use_container_width=True)
        else:
            columnNames = st.sidebar.selectbox('Column Names', options)
            st.write('Select the column you want the line chart to display')
            st.write('')
            st.write('Chart:')
            plotGraph(st.line_chart, columnNames, st, df[0:size])
    
    elif select == 'Bar Chart':
    
        select2 = st.sidebar.selectbox('Customize Bar Chart', ['No', 'Yes'])

        if select2 == 'Yes':
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index
                
            x_axis = st.sidebar.selectbox('X Axis', listOfColumnNames)
            y_axis = st.sidebar.selectbox('Y Axis', listOfColumnNames)

            color = st.sidebar.selectbox('Change color based of value?', ['No', 'Yes'])
            size = st.sidebar.selectbox('Change width based of value?', ['No', 'Yes'])
            tooltips =st.sidebar.multiselect('Tooltips (select more than one', listOfColumnNames)

            title = st.text_input('Chart Title')
            width = st.number_input('Width', step=10, min_value=200, max_value=1000)
            height = st.number_input('Height', step=10, min_value=400, max_value=1000)
            
            if color == 'Yes':
                if size == 'Yes':
                    c = alt.Chart(new_df).mark_bar().encode(
                        x=x_axis, y=y_axis, 
                        size=y_axis, 
                        color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
                else:
                    c = alt.Chart(new_df).mark_bar().encode(
                        x=x_axis, y=y_axis, 
                        #size=y_axis, 
                        color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )

            else:
                if size == 'Yes':
                    c = alt.Chart(new_df).mark_bar().encode(
                        x=x_axis, y=y_axis, 
                        size=y_axis, 
                        #color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
                else:
                    c = alt.Chart(new_df).mark_bar().encode(
                        x=x_axis, y=y_axis, 
                        #size=y_axis, 
                        #color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
            st.write('')
            st.write('Chart:')       
            st.altair_chart(c, use_container_width=True)
        else:
            columnNames = st.sidebar.selectbox('Choose a column to display', options)
            st.write('Select the column you want the line chart to display')
            plotGraph(st.bar_chart, columnNames, st, df)
    elif select == 'Scatter Plot':
        select2 = st.sidebar.selectbox('Customize Bar Chart', ['No', 'Yes'])

        if select2 == 'Yes':
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index
                
            x_axis = st.sidebar.selectbox('X Axis', listOfColumnNames)
            y_axis = st.sidebar.selectbox('Y Axis', listOfColumnNames)

            color = st.sidebar.selectbox('Change color based of value?', ['No', 'Yes'])
            size = st.sidebar.selectbox('Change width based of value?', ['No', 'Yes'])
            tooltips =st.sidebar.multiselect('Tooltips (select more than one', listOfColumnNames)

            title = st.text_input('Chart Title')
            width = st.number_input('Width', step=10, min_value=200, max_value=1000)
            height = st.number_input('Height', step=10, min_value=400, max_value=1000)
            
            c = alt.Chart(df).mark_circle().encode(
                x=x_axis, y=y_axis, size=y_axis, color=y_axis, tooltip=tooltips).properties(
                            title=title,
                            width=width,
                            height=height
                            )
            st.write('')
            st.write('Chart:')
            st.altair_chart(c, use_container_width=True)
        else:
            
            columnNames = st.sidebar.selectbox('Choose a column to display', options)
            st.write('Select the column you want the line chart to display')
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index
                c = alt.Chart(new_df).mark_circle().encode(
                    x=df.index.name, y=columnNames)
                st.altair_chart(c, use_container_width=True)
            else:
                new_df['-index-'] = [x for x in range(1,len(df)+1)]
                c = alt.Chart(new_df).mark_circle().encode(
                    x='-index-', y=columnNames)
                st.write('')
                st.write('Chart:')
                st.altair_chart(c, use_container_width=True)
        
def sampleOption(df, st):
    sampleSelect = st.sidebar.selectbox('Whole or Sample', ['Sample for dataframe', 'Whole dataframe'])
    if sampleSelect == 'Sample for dataframe':
        size = st.number_input('Enter the sample size', min_value=1, step=1, max_value=len(df))
    
        sampleSelect2 = st.sidebar.selectbox('Sample', ['Sample from top', 'Sample from bottom', 'Random sample'])
        if sampleSelect2 == 'Sample from top':
           st.write('Here is a sample of ', size,' from the top')
           st.dataframe(df.head(size), height=450)
        elif sampleSelect2 == 'Sample from bottom':
           st.write('Here is a sample of ', size,' from the bottom')
           st.dataframe(df.tail(size), height=450)
        elif sampleSelect2 == 'Random sample':
           st.write('Here is a random sample of ', size)
           st.dataframe(df.sample(size), height=450)        
          
    elif sampleSelect == 'Whole dataframe':
        st.write('Here is the whole dataframe')
        st.dataframe(df, height=580)
        
def getSubheader(st):
    st.subheader("File has been successfully added.")
    st.subheader("Select yes to begin MIDAC")
    
def author():
    from PIL import Image
    import webbrowser

    image = Image.open('assets/eniola.jpeg')
    st.image(image ,width=200, caption="Author: Eniola Osineye")
    st.subheader('Hi There!')
    st.subheader('My name is Eniola Osineye and I am currently a computer science senior at Walsh University and a future software engineer and data analyst. This is MIDAC, it is my data analytics minor senior project for the CS398 Data Analytics Practicum class.')
    st.subheader('The aim of MIDAC is to help in small business decisions by utilizing data to drive those decisions.')
    st.subheader('*Problem*: Over my years as a data analytics minor, I realised that to analyze data, one must have a basic knowledge of data analytics tools such as excel and/or python/R. However, most business manager may not have the knowledge needed to operate these tools effectively and may require a data analyst. However, some business decisions are minor/small and do not utiize the full capacity of the data analyst. That\'s where MIDAC comes in.')
    st.subheader('*Solution*: MIDAC aims to allow managers to quickly generate visual represntaion and information from data which can be used to drive business decisions. Moreover, MIDAC is fast, efficent, and user-friendly, which gives everyone the ability to be a data analyst in seconds.')
    st.subheader("Have *fun* :sunglasses: \nEniola Osineye")
    
    linkedin = 'https://www.linkedin.com/in/eniola-osineye-68480b146/'
    
    if st.button('My portfolio'):
        webbrowser.open_new_tab('http://www.osineye.com')

   
    if st.button('Connect on LinkedIn'):
        webbrowser.open_new_tab(linkedin)
        
    st.button('Connect by email: osineye70@gmail.com')
    