# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 13:47:44 2022

@author: martyna1221
"""

"""

    Google Sheet & BQ functions :
        (1) Google Sheets connection which requires only the link to the
            Google Sheet and the sheet name (i.e. the name of the tab which is
            located in the bottom left corner; initialized to 'Sheet1' unless
            manually changed); returns the spreadsheet as a table via pandas
        (2) BQ function which grabs all table names (project.dataset.table) 
            from a specific dataset in BQ project
        (3) Query BQ tables that have a specific column name


"""

import re # TODO: pip install regex
import pandas as pd # TODO: pip install pandas

# (1) Google Sheets connection

def open_google_sheet(sheet_link, sheet_name):
    # searches for the sheet_id from the given GS url
    match = re.search(r'd/([a-zA-Z0-9-_]+)', sheet_link)
    sheet_id = match.group()
    sheet_id = sheet_id[2:]
    # inputs the searched sheet_id and the given sheet_name in an f-string
    url_to_open = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}'
    # reads the GS as a csv and turns it into a pandas dataframe
    google_sheet_df = pd.read_csv(url_to_open)
    return google_sheet_df

# go to https://docs.google.com/spreadsheets/d/1a2zZKqy5H8Ia56x7LQwXI4LJAY_BcvSmN7bdamFoJ94/edit#gid=356742440
# on your browser of choice; when creating your spreadsheet make sure that you
# share the sheet so that anyone with the link is able to view it

# this dataset was found on https://condor.depaul.edu/sjost/it223/datasets.htm; 
# visit that url for more information

# this is a dataset of the 1985 Chicago Bears roster imported into a Python
# environment as a pandas dataframe

df = open_google_sheet(sheet_link = 'https://docs.google.com/spreadsheets/d/1a2zZKqy5H8Ia56x7LQwXI4LJAY_BcvSmN7bdamFoJ94/edit#gid=356742440',
                       sheet_name = 'Sheet1')

# options set so that the full table can be seen when printed to the console
pd.set_option('display.expand_frame_repr', False)
# prints the first 5 entries in the dataframe
print(df.head(5))

# (2) BQ function that collects names of all tables from a specific datatset
# within a given project

import pandas_gbq # TODO: pip install pandas-gbq

dataset = # TODO: add datset name here (i.e. project.{dataset}.table)
project = # TODO: add project name here (i.e. {project}.dataset.table)

# more information about pandas_gbq can be found here https://pandas-gbq.readthedocs.io/en/latest/index.html

# returns table_names as a dataframe
def get_BQ_table_names(dataset, project):
    table_names = pandas_gbq.read_gbq(f'SELECT TABLE_NAME from `{project}.{dataset}.INFORMATION_SCHEMA.TABLES`', project_id = project)
    return table_names

table_names = get_BQ_table_names(dataset = dataset,
                                 project = project)

# (3) BQ function that finds tabes in a datset within a project with a certain
# keyword as a column (for example, finding all tables with a column called 
# 'Email' in project.dataset)

# you can use the dataframe that is outputted from the above function as your
# input for the below function; they work hand in hand

df_of_tables = table_names # TODO OPTIONAL: add a df of table names
data_set = # TODO: add datset name here (i.e. project.{dataset}.table)
keyword = # TODO: add keyword here (i.e. 'Email' OR 'Age')
project = # TODO: add project name here (i.e. {project}.dataset.table)

def get_BQ_tables_to_query(df_of_tables, dataset, keyword, project):
    df_of_tables_to_list = df_of_tables['TABLE_NAME'].values.tolist()
    # the count variable shows the user how many tables the program runs through
    count = 1
    for x in df_of_tables['TABLE_NAME'].values.tolist():
        # gets the table name from df_of_tables
        table = str(x)
        # SQL query which gets column names from a specific table
        cols = pandas_gbq.read_gbq(f'SELECT COLUMN_NAME from `{project}.{dataset}.INFORMATION_SCHEMA.COLUMNS` WHERE table_name = \'{table}\'')
        # converts cols variable from a dataframe to a list
        col_list = cols['COLUMN_NAME'].values.tolist()
        # checks to see if keyword is in the list of column names
        if (keyword in col_list):
            print(f'{count}: the table named {table} contains a column called {keyword}')
        else:
            # if keyword is not found in the list of column names, the table
            # is taken out of the list
            df_of_tables_to_list.remove(table)
            print(f'{count}: the table named {table} DOES NOT contain a column called {keyword}')
        count += 1
    # returns a list of tables that contain the specified keyword within a 
    # given project.dataset
    return df_of_tables_to_list
        
table_list = get_BQ_tables_to_query(df_of_tables = df_of_tables,
                                    dataset = dataset, 
                                    keyword = keyword,
                                    project = project)
