# Imports from function.py
from functions import graphOption, sampleOption, getSubheader, author,  displayImageAndTitle, getHelpDetails
from functions import welcomeText, lengthOption, getDataColumnNames, describeData, showVideo

# Import streamlit library
import streamlit as st

# Import pandas library for datafram
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np


import altair as alt



def createRecord(df, st):
    newRecord = {}
                        
    for x in getDataColumnNames(df):
        try:
            int(df[x][0])
            inputBox = st.number_input('Enter value for {}'.format(x), step=0.5)
        except:
            inputBox = st.text_input('Enter value for {}'.format(x))

        newRecord[x] = inputBox

    if st.button('Add record'):
        df = df.append(newRecord, ignore_index=True)
        st.write('Record has been added successfully.')


# Display Walsh logo and title
displayImageAndTitle(st)

# Main menu options
helpOptions = st.sidebar.selectbox('Select start to start SAM', ['Welcome', 'Start', 'Help', 'Author'])

# Welcome option
if helpOptions == 'Welcome':
    welcomeText(st)
    
# Start option    
elif helpOptions == 'Start':
    try:
        uploaded_file = st.sidebar.file_uploader("Choose a file")
    except Exception as e:
        st.write(e)
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            listOfColumnNames = [item for item in getDataColumnNames(df)]
            listOfColumnNames.sort()
            start = st.sidebar.selectbox('Start', ['No', 'Yes'])
            uniqueColumns = ['None']
            for col in df.columns:
                if df[col].is_unique:
                    uniqueColumns.append(col)
                    
            indexColumn = st.sidebar.selectbox('Set Index from unique columns', uniqueColumns)
            
            if indexColumn != 'None':
                df = df.set_index(df[indexColumn])
                options = []
                for name in listOfColumnNames:
                    try: 
                        int(df[name][0])
                        options.append(name)
                    except:
                        pass
                if len(options) == 0:
                    st.subheader('This index is not recommended as it may affect some of my functionalities.')
                
                df.drop([indexColumn], inplace=True, axis=1)
            elif indexColumn == 'None':
                df.reset_index()
                df.index = [x for x in range(len(df))]
            
            
            if start == 'No':
                getSubheader(st)
            
            elif start == 'Yes':
                
                mainOptions =  st.sidebar.selectbox('Main Options', ['Get Sample', 'Get Length', 'Draw Graph', 'Describe Data'])
            
                if mainOptions == 'Get Sample':
                    try: 
                        sampleOption(df, st)
                    except:
                        st.warning('Opps something went wrong 🥺')
                    
                elif mainOptions == 'Get Length':
                    try:
                        lengthOption(st, listOfColumnNames, df)
                    except:
                        st.warning('Opps something went wrong 🥺')
    
                elif mainOptions == 'Draw Graph':
                    try:
                        graphOption(st, listOfColumnNames, df, indexColumn)
                    except Exception as e:
                        st.write(e)
                        st.warning('Opps something went wrong 🥺')
                
                elif mainOptions == 'Describe Data':
                    try: 
                        describeData(st, df, listOfColumnNames)
                    except:
                        st.warning('Opps something went wrong 🥺')
                
        except Exception as e:
            st.warning('File upload failed. The file must be a csv file less than 200MB')
            
          
# Help option selected
elif helpOptions == 'Help':
    getHelpDetails(st)

# Author option selected
elif helpOptions == 'Author':
    author()
    

 
            
