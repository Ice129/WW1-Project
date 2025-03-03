# Here is a list of backend functions that will be implemented according to our API design.
# These functions will be exclusively accessed from inside this file, or from api.py.
# The database instance will only be accessed from this file.
#####################################################################################################################################
# The below database connection will be the only one used in this file.
# If you need to reset the cursor, you can do so by calling cursor.close() and then cursor = database.cursor()
# If you need to reset the database, you can do so by calling database.close() and then database = sqlite3.connect("database.db")
# Only do this if necessary and do it in your own functions.
import sqlite3
database = sqlite3.connect("database.db")
cursor = database.cursor()

# Assigned to: Charlie
# This function will load a XLSX file from a given location and return it as a dictionary
import openpyxl
from io import BytesIO
def load_xlsx(fileLocation: str, fileBytes: bytes = None) -> dict:
    # Load the workbook
    if fileBytes is None:
        workbook = openpyxl.load_workbook(fileLocation)
    else:
        workbook = openpyxl.load_workbook(BytesIO(fileBytes))
    
    # Initialize the dictionary to store the data
    data_dict = {}
    
    # Iterate through each sheet in the workbook
    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        
        # Initialize a list to store rows for the current sheet
        rows = []
        
        # Iterate through each row in the sheet
        for row in sheet.iter_rows(values_only=True):
            # Append the row (as a tuple) to the rows list
            rows.append(row)
        
        # Add the rows list to the dictionary with the sheet name as the key
        data_dict[sheet_name] = rows
    
    return data_dict

# Assigned to: Hope
# This function will instantiate the databases as well as their columns for the next function, insert_to_sql()
def create_database():
    return True

# Assigned to: Charlie
# This function will call the load_csv() on all of the csv files in the directory
# It will then convert their returned values into the created SQL databases in create_database()
def insert_to_sql(sheetData: dict) -> bool:
    # Detect which database the data belongs in
    desiredTable = ""

    return True

# Assigned to: ???
# This function will add a singular row to the SQL database
def singular_add_sql(dataObject: dict, databaseName: str):
    return True

# Do not edit any code below this point.
# Only edit code you have been assigned in this project.
if __name__ == "__main__":
    create_database()
    insert_to_sql()
    exit()

#test
