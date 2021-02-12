#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 21:25:36 2021

@author: eniolaosineye
"""

# Imports from function.py
from functions import graphOption, sampleOption, getSubheader, author,  displayImageAndTitle
from functions import welcomeText, lengthOption, getDataColumnNames, describeData

# Import streamlit library
import streamlit as st

# Import pandas library for datafram
import pandas as pd

#df = df.set_index(df[listOfColumnNames[0]])
#df.drop([listOfColumnNames[0]], inplace=True, axis=1)

# Display Walsh logo and title
displayImageAndTitle(st)

# Main menu options
helpOptions = st.sidebar.selectbox('Select start to start Midac', ['Welcome', 'Start', 'Help', 'Author'])

# Welcome option
if helpOptions == 'Welcome':
    welcomeText(st)
    
# Start option    
elif helpOptions == 'Start':
    uploaded_file = st.sidebar.file_uploader("Choose a file")
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
                        st.write('Opps something went wrong 🥺')
                    
                elif mainOptions == 'Get Length':
                    try:
                        lengthOption(st, listOfColumnNames, df)
                    except:
                        st.write('Opps something went wrong 🥺')
    
                elif mainOptions == 'Draw Graph':
                    try:
                        graphOption(st, listOfColumnNames, df)
                    except:
                        st.write('Opps something went wrong 🥺')
                
                elif mainOptions == 'Describe Data':
                    try: 
                        describeData(st, df, listOfColumnNames)
                    except:
                        st.write('Opps something went wrong 🥺')
                    
        except:
            st.write('File upload failed. The file must be a csv file less than 200MB')
          
# Help option selected
elif helpOptions == 'Help':
    pass

# Author option selected
elif helpOptions == 'Author':
    author()
    

 
            
