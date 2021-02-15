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

#Returns whether a variable's type is int or not
def is_int(val):
    if type(val) == int:
        return True
    else:
        if val.is_integer():
            return True
        else:
            return False

# Helper function to display describtive statistics about dataframe      
def displayStatistics(func, column, trigger, df):
    try:
        st.write('The ', trigger, ' of ', column, ' is: ', func(column, df))     
    except:
        st.warning('The column you choice does not exist in the dataframe')
            
# Help function to plot different charts
def plotGraph(func, column, st, df):
    try:
        func(df[column])
       
    except:
        st.warning('The column you choice does not exist in the dataframe')
        
#Helper function to display logo and title
def displayImageAndTitle(st):
    from PIL import Image
    logo = Image.open('assets/logo/logo.png')
    st.image(logo ,width=200)   
    st.title("(S)imple (A)nalysis (M)achine")
    st.sidebar.title("SAM")
    st.sidebar.markdown("Please click on an options below:")
        
# Welcome option text
def welcomeText(st):
    st.header('Hello, *World!* :sunglasses:')
    st.subheader("I'm SAM, which stands for simple analysis machine. I am here to help you analyze data quickly and derive information to aid in small business descisions.")
    st.subheader("To get started, just select *start* from the selecbox is the side bar on the left.")
    st.subheader("Have *fun,* \nEniola Osineye :smile:") 

def describeData(st, df, listOfColumnNames):
    #Importing necessary libary
    import pandas as pd

    select = st.sidebar.selectbox('Select an option', ['Sum', 'Quartile','Median', 'Lowest', 'Highest', 'Mean', 'Variance', 'Standard Deviation', 'Comprehensive'])   
    options = []

    # Adding column names to list if the column type is numeric to display in selectbox
    for name in listOfColumnNames:
        try: 
            int(df[name][0])
            options.append(name)
        except:
            pass
    
    # Get sum of all values in column
    if select == 'Sum':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getSumOfColumn, columnNames, 'sum', df)
        
    # Get quartile data out of all data in column
    elif select == 'Quartile':
        columnNames = st.sidebar.selectbox('Column Names', options)
        st.write('The quartiles of ', columnNames, ' is:')
        s = getQuantileOfColumn(columnNames, df)
        
        #Setting index of quartile data
        s.index = ['1st', '2nd', '3rd', '4th']
        st.write(s)

    # Get median value out of all data in column  
    elif select == 'Median':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMedianOfColumn, columnNames, 'median', df)
            
    # Get lowest value or rrecord of highest value out of all data in column
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
                  
    # Get highest value or record of highest value out of all data in column
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

    # Get mean of all values in column    
    elif select == 'Mean':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getMeanOfColumn, columnNames, 'mean', df)

    # Get variance of all values in column
    elif select == 'Variance':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getVarOfColumn, columnNames,  'variance', df)
        
    # Get standard deviation of all values in column
    elif select == 'Standard Deviation':
        columnNames = st.sidebar.selectbox('Column Names', options)
        displayStatistics(getStdOfColumn, columnNames, 'standard deviation', df)

    # Get comprehensive statistics of all values in column
    elif select == 'Comprehensive':
        columnNames = st.sidebar.selectbox('Column Names', options)
        st.write(df[columnNames].describe())
                  
   
# Display length of whole dataframe or column in dataframe
def lengthOption(st, listOfColumnNames, df):
    options = ['All (length for all columns)']
    
    for name in listOfColumnNames:
        options.append(name)
    
    columnNames = st.sidebar.selectbox('Column Names', options)

    if columnNames == 'All (length for all columns)':
        st.write('The length of the whole dataframe is: ', len(df))
    else:
        st.write('The length of column ', columnNames, ' in the dataframe is: ', getLength(columnNames, df))

# Helper function to visualize date in main option selectbox
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
    
    # Display area chart
    if select == 'Area Chart':
        select2 = st.sidebar.selectbox('Customize Area Chart', ['No', 'Yes'])

        # Set size of sample size
        size = st.sidebar.number_input('Sample size', step=1, min_value=1, max_value=len(df))

        # Display customized area chart
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
            c = alt.Chart(new_df[0:size]).mark_area(
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
                    alt.Y(y_axis),
                    tooltip= tooltips
                ).properties(
                    title=title,
                    width=width,
                    height=height
                )
            st.write('')
            st.write('Chart:')
            st.altair_chart(c, use_container_width=True)
        
        # Display simple area chart
        else:
            columnNames = st.sidebar.selectbox('Column Names', options)
            st.write('Select the column you want the area chart to display')
            st.write('')
            st.write('Chart:')
            plotGraph(st.area_chart, columnNames, st, new_df[0:size])
        
    # Display line chart
    elif select == 'Line Chart':
        select2 = st.sidebar.selectbox('Customize Line Chart', ['No', 'Yes'])

        # Set size of sample size
        size = st.sidebar.number_input('Sample size', step=1, min_value=1, max_value=len(df))
        
        #Display customized line chart
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
        
        # Display simple line chart
        else:
            columnNames = st.sidebar.selectbox('Column Names', options)
            st.write('Select the column you want the line chart to display')
            st.write('')
            st.write('Chart:')
            plotGraph(st.line_chart, columnNames, st, df[0:size])
    
    # Display bar chart
    elif select == 'Bar Chart':
        select2 = st.sidebar.selectbox('Customize Bar Chart', ['No', 'Yes'])

        # Set size of sample size
        size = st.sidebar.number_input('Sample size', step=1, min_value=1, max_value=len(df))

        # Display customized bar chart
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
                    c = alt.Chart(new_df[0:size]).mark_bar().encode(
                        x=x_axis, 
                        y=y_axis, 
                        size=y_axis, 
                        color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
                else:
                    c = alt.Chart(new_df[0:size]).mark_bar().encode(
                        x=x_axis, 
                        y=y_axis, 
                        color=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )

            else:
                if size == 'Yes':
                    c = alt.Chart(new_df[0:size]).mark_bar().encode(
                        x=x_axis, 
                        y=y_axis, 
                        size=y_axis,  
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
                else:
                    c = alt.Chart(new_df[0:size]).mark_bar().encode(
                        x=x_axis, 
                        y=y_axis, 
                        tooltip=tooltips).properties(
                        title=title,
                        width=width,
                        height=height
                        )
            st.write('')
            st.write('Chart:')       
            st.altair_chart(c, use_container_width=True)
        
        # Display simple bar chart
        else:
            columnNames = st.sidebar.selectbox('Choose a column to display', options)
            st.write('Select the column you want the bar chart to display')
            st.write('')
            plotGraph(st.bar_chart, columnNames, st, new_df[0:size])
    
    # Display scatterplot
    elif select == 'Scatter Plot':
        select2 = st.sidebar.selectbox('Customize Scatter Plot', ['No', 'Yes'])

        # Set size of sample size
        size = st.sidebar.number_input('Sample size', step=1, min_value=1, max_value=len(df))

        # Display customized scatterplot
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
            
            c = alt.Chart(new_df[0:size]).mark_circle().encode(
                x=x_axis, y=y_axis, size=y_axis, color=y_axis, tooltip=tooltips).properties(
                            title=title,
                            width=width,
                            height=height
                            )
            st.write('')
            st.write('Chart:')
            st.altair_chart(c, use_container_width=True)
        
        # Display simple scatterplot
        else:
            
            columnNames = st.sidebar.selectbox('Choose a column to display', options)
            st.write('Select the column you want the line chart to display')
            new_df = df
            if indexColumn != 'None':
                new_df[df.index.name] = df.index
                c = alt.Chart(new_df[0:size]).mark_circle().encode(
                    x=df.index.name, y=columnNames)
                st.write('')
                st.write('Chart:')
                st.altair_chart(c, use_container_width=True)
            else:
                new_df['-index-'] = [x for x in range(1,len(df)+1)]
                c = alt.Chart(new_df[0:size]).mark_circle().encode(
                    x='-index-', y=columnNames)
                st.write('')
                st.write('Chart:')
                st.altair_chart(c, use_container_width=True)

# Helper function for get sample section in main option selectbox  
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
        
# Helper function to indicate when a video has been successfully uploaded
def getSubheader(st):
    st.subheader("File has been successfully added.")
    st.subheader("Select yes to begin SAM")

# Helper function to display images and text in author section   
def author():
    from PIL import Image
    import webbrowser

    image = Image.open('assets/eniola.jpeg')
    st.image(image ,width=200, caption="Author: Eniola Osineye")
    st.subheader('Hi There!')
    st.subheader('My name is Eniola Osineye and I am currently a computer science senior at Walsh University and a future software engineer and data analyst. This is SAM(simple analysis machine), it is my data analytics minor senior project for the CS398 Data Analytics Practicum class.')
    st.subheader('The aim of SAM is to help in small business decisions by utilizing data to drive those decisions.')
    st.subheader('*Problem*: Over my years as a data analytics minor, I realised that to analyze data, one must have a basic knowledge of data analytics tools such as excel and/or python/R. However, most business manager may not have the knowledge needed to operate these tools effectively and may require a data analyst. However, some business decisions are minor/small and do not utiize the full capacity of the data analyst. That\'s SAM comes in.')
    st.subheader('*Solution*: SAM aims to allow managers to quickly generate visual represntaion and information from data which can be used to drive business decisions. Moreover, SAM is fast, efficent, and user-friendly, which gives everyone the ability to be a data analyst in seconds.')
    st.subheader("Have *fun* :sunglasses: \nEniola Osineye")
    
    linkedin = 'https://www.linkedin.com/in/eniola-osineye-68480b146/'
    
    if st.button('My portfolio'):
        webbrowser.open_new_tab('http://www.osineye.com')

   
    if st.button('Connect on LinkedIn'):
        webbrowser.open_new_tab(linkedin)
        
    st.button('Connect by email: osineye70@gmail.com')
    

# Helper function to display videos
def showVideo(url, st):
    video_file = open(url, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)


# Helper function to display instructions in help section
def getHelpDetails(st):
    option = st.sidebar.selectbox('FAQ', ['How to upload a CSV file?', 'How to start SAM?', 'Assign index to data frame?', 'Display sample or whole data frame?', 'Length of column or whole data frame?', 'Visualize data and draw graphs?', 'How to statistically describe data?'])

    if option == 'How to upload a CSV file?':
        st.subheader('How to upload a CSV file:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from Select start to start *SAM* select box')
        st.write('3) Click the browse file button in the upload file card')
        st.write('4) Locate CSV file to upload and select a file')
        st.write('5) When your file is successfully uploaded, select *Yes* from Start select box')
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/csv.mp4', st)

    elif option == 'How to start SAM?':
        st.subheader('How to start SAM:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then, select *Yes* from *Start* select box')
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/start.mp4', st)
        
    elif option == 'Assign index to data frame?':
        st.subheader('How to assign index to data frame:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then select *Yes* from *Start* select box')
        st.write('5) The *Set Index from unique columns* select box display all in the unique column in the data frame' )
        st.write('6) Not every column display should be used, select whichever column would be the best for your analysis' )
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/index.mp4', st)
    elif option == 'Display sample or whole data frame?':
        st.subheader('How to display sample or whole data frame:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then select *Yes* from *Start* select box')
        st.write('5) Select *Get Sample* from *Main Options* select box. Two select boxes will appear below' )
        st.write('6) To get a sample of the data frame, select *Sample of data frame* from *Whole or Sample* select box and to display whole data frame, select *Whole data frame* from *Whole or Sample*' )
        st.write('7) When selecting a sample, you have the option to select from the head or bottom of the data frame, or a random sample of the data frame')
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/sample.mp4', st)
    elif option == 'Length of column or whole data frame?':
        st.subheader('How to get the length of column or whole data frame:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then select *Yes* from *Start* select box')
        st.write('5) Select *Get Length* from *Main Options* select box. A select box will appear below' )
        st.write('6) To get the length of the whole data frame, select *All* from *Column Names* select box and to get the length of a column in the data frame, select the column from the *Column Names* select box' )
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/length.mp4', st)
    elif option == 'Visualize data and draw graphs?':
        st.subheader('How to visualize data and draw graphs:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then select *Yes* from *Start* select box')
        st.write('5) Select *Draw Graph* from *Main Options* select box. Three select boxes will appear below' )
        st.write('6) In the *Pick a graph* select box, you can select which chart you want. The *Customize Bar chart* asks whether you want a simple or customized chart.')
        st.write('7) For a simple chart, select *No* and select the column you want as the Y-axis from *Column Names* select box')
        st.write('8) By selecting *Yes* to customize the chart, you can now select what column should be plotted on the Y-axis and X-axis, and add tooltips to see more data about a record in the chart')
        st.write('9) Also, some charts allow you to change the color of the chart and add tooltips to see more data about the record')
        st.write('10) Finally, you can save the graph as a PNG or SVG by clicking the three dots on the top right corner of the chart')
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/chart.mp4', st)
    elif option == 'How to statistically describe data?':
        st.subheader('How to statistically describe data:')
        st.write('1) Open sidebar')
        st.write('2) Select *Start* from *Select start to start SAM* select box')
        st.write('3) Upload a CSV file successfully')
        st.write('4) Then select *Yes* from *Start* select box')
        st.write('5) Select *Describe Data* from *Main Options* select box. Two select boxes will appear below' )
        st.write('6) The *Select an option* select box allows you to select what type of statistic you want. Select comprehensive, if you want to see all statistics at once' )
        st.write('7) The *Column Names* select box is where you select which column in the data frame that you want the statistics to be performed on')
        st.write('8) If you select the *Lowest* or *Highest* option from the *Select an option* select box, there will be another select box, *Show record(s)*, that allows you to show the record(s) the lowest/highest in the column chosen')
        st.write('9) You can select *Yes* from the *Show record(s)* select box which will allow you to show the entire record or just the column selected')
        st.write('')
        st.write('Need more help? Watch the video below:')
        showVideo('assets/videos/describe.mp4', st)