# BQ_and_GS_Functions
1 Google Sheets function that pulls a Google Sheet into a Python environment; 2 Big Query functions; (1) queries tables names from a dataset and (2) queries table names from a dataset that contain a specific column.

    Google Sheet & BQ functions :
        (1) Google Sheets connection which requires only the link to the
            Google Sheet and the sheet name (i.e. the name of the tab which is
            located in the bottom left corner; initialized to 'Sheet1' unless
            manually changed); returns the spreadsheet as a table via pandas
        (2) BQ function which grabs all table names (project.dataset.table) 
            from a specific dataset in BQ project
        (3) Query BQ tables that have a specific column name
