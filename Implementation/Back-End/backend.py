# Here is a list of backend functions that will be implemented according to our API design.
# These functions will be exclusively accessed from inside this file, or from api.py.
# The database instance will only be accessed from this file.
#####################################################################################################################################
# The below database connection will be the only one used in this file.
# If you need to reset the cursor, you can do so by calling cursor.close() and then cursor = database.cursor()
# If you need to reset the database, you can do so by calling database.close() and then database = sqlite3.connect("database.db")
# Only do this if necessary and do it in your own functions.
import sqlite3
import pandas as pd
import xlsxwriter
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

# Assigned to: Edward
#This function will make a .xlsx file from the online database
def download_xlsx():
    #grabbing data from the database


    # NewspaperReferences2025 database
    cursor.execute("SELECT * FROM NewspaperReferences2025")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
    HeadersWithData = {}
    for num in range(len(Headers)-1):
        HeadersWithData = {**HeadersWithData, Headers[num+1]: [d[num+1] for d in Data]}
    df = pd.DataFrame(HeadersWithData)
    writer = pd.ExcelWriter("NewspaperReferences2025.xlsx",engine="xlsxwriter")
    df.to_excel(writer,sheet_name="sheet1",index=False)
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]
    worksheet.autofit()
    workbook.close()

    # RollOfHonour
    cursor.execute("SELECT * FROM RollOfHonour")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
    HeadersWithData = {}
    for num in range(len(Headers) - 1):
        HeadersWithData = {**HeadersWithData, Headers[num + 1]: [d[num + 1] for d in Data]}
    df = pd.DataFrame(HeadersWithData)
    writer = pd.ExcelWriter("RollOfHonour.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]
    worksheet.autofit()
    workbook.close()

    # BiographySpreadsheet
    cursor.execute("SELECT * FROM BiographySpreadsheet")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
    HeadersWithData = {}
    for num in range(len(Headers) - 1):
        HeadersWithData = {**HeadersWithData, Headers[num + 1]: [d[num + 1] for d in Data]}
    df = pd.DataFrame(HeadersWithData)
    writer = pd.ExcelWriter("BiographySpreadsheet.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]
    worksheet.autofit()
    workbook.close()

    # BradfordMemorials
    cursor.execute("SELECT * FROM BradfordMemorials")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
    # print(Headers)
    # print (Data)
    # splitting data
    HeadersWithData = {}
    for num in range(len(Headers) - 1):
        HeadersWithData = {**HeadersWithData, Headers[num + 1]: [d[num + 1] for d in Data]}
    df = pd.DataFrame(HeadersWithData)
    writer = pd.ExcelWriter("BradfordMemorials.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]
    worksheet.autofit()
    workbook.close()

    # BuriedInBradford
    cursor.execute("SELECT * FROM BuriedInBradford")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
    # print(Headers)
    # print (Data)
    # splitting data
    HeadersWithData = {}
    for num in range(len(Headers) - 1):
        HeadersWithData = {**HeadersWithData, Headers[num + 1]: [d[num + 1] for d in Data]}
    df = pd.DataFrame(HeadersWithData)
    writer = pd.ExcelWriter("BuriedInBradford.xlsx", engine="xlsxwriter")
    df.to_excel(writer, sheet_name="sheet1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]
    worksheet.autofit()
    workbook.close()




# Assigned to: Hope
# This function will instantiate the databases as well as their columns for the next function, insert_to_sql()
def create_database ():

    cursor.execute("""
        CREATE TABLE biographyspreadsheet (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            regiment VARCHAR(70),
            service_number VARCHAR(40),
            biography_attachment VARCHAR(300)
        );
    """)

    cursor.execute("""
        CREATE TABLE bradfordmemorials (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80) ,
            regiment VARCHAR(70),
            unit VARCHAR(40),
            memorial VARCHAR(150),
            memorial_location VARCHAR(150),
            memorial_info VARCHAR(150),
            memorial_postcode VARCHAR(32),
            district VARCHAR(150),
            photo_available BOOLEAN
        );
     """)

    cursor.execute("""
        CREATE TABLE buriedinbradford (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            age INT(3),
            medals LONGTEXT,
            date_of_birth DATE,
            rank VARCHAR(40),
            unit VARCHAR(40),
            cemetery VARCHAR(150),
            grave_ref VARCHAR(40),
            info LONGTEXT
        );
     """)

    cursor.execute("""
        CREATE TABLE memorialnames (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            memorial VARCHAR(150)
         );
    """)

    cursor.execute("""
        CREATE TABLE newspaperreferences2025 (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            rank VARCHAR(40),
            address VARCHAR(150),
            regiment VARCHAR(70),
            unit VARCHAR(40),
            article_comment VARCHAR(300),
            newspaper_name VARCHAR(150),
            newspaper_date DATE,
            page_col VARCHAR(10),
            photo_incl BOOLEAN
        );
     """)

    cursor.execute("""
        CREATE TABLE rollofhonour (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            address VARCHAR(150),
            electoral_ward VARCHAR(35),
            town VARCHAR(35),
            rank VARCHAR(40),
            regiment VARCHAR(70),
            unit VARCHAR(40),
            company VARCHAR(40),
            age INT(3),
            service_no VARCHAR(40),
            other_regiment VARCHAR(70),
            other_service_no VARCHAR(40),
            medals LONGTEXT,
            enlisted_date DATE,
            discharged_date DATE,
            death_date DATE,
            misc_info_nroh VARCHAR(200),
            cemetery_memorial VARCHAR(150),
            cemetery_memorial_ref VARCHAR(40),
            cemetary_memorial_country VARCHAR(56),
            additional_cwgc_info VARCHAR(300)
        );
     """)

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
    download_xlsx()
    exit()


