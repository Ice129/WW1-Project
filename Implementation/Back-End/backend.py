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
def load_xlsx(fileLocation: str = "", fileBytes: bytes = None) -> dict:
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

    #grabbing data from the database


    #if place_holder_check

    # NewspaperReferences2025 database
def DLNewspaperReferences2025():
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
def DLRollOfHonour():
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
def DLBiographySpreadsheet():
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
def DLBradfordMemorials():
    cursor.execute("SELECT * FROM BradfordMemorials")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
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
def DLBuriedInBradford():
    cursor.execute("SELECT * FROM BuriedInBradford")
    Data = cursor.fetchall()
    Headers = [description[0] for description in cursor.description]
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
        CREATE TABLE IF NOT EXISTS biographyspreadsheet (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            regiment VARCHAR(70),
            service_number VARCHAR(40),
            biography_attachment VARCHAR(300)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bradfordmemorials (
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
        CREATE TABLE IF NOT EXISTS buriedinbradford (
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
        CREATE TABLE IF NOT EXISTS memorialnames (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            surname VARCHAR(80),
            forename VARCHAR(80),
            memorial VARCHAR(150)
         );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS newspaperreferences2025 (
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
        CREATE TABLE IF NOT EXISTS rollofhonour (
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
    desired_table = detect_table(sheetData)

    insert_statements = {
        "BradfordMemorials": "INSERT INTO BradfordMemorials (surname, forename, regiment, unit, memorial, memorial_location, memorial_postcode, district, photo_available) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
        "NewspaperReferences2025": "INSERT INTO NewspaperReferences2025 (surname, forename, rank, address, regiment, unit, article_comment, newspaper_name, newspaper_date, page_col, photo_incl) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
        "BiographySpreadsheet": "INSERT INTO BiographySpreadsheet (surname, forename, regiment, service_number, biography_attachment) VALUES (?, ?, ?, ?, ?);",
        "RollOfHonour": "INSERT INTO RollOfHonour (surname, forename, address, electoral_ward, town, rank, regiment, unit, company, age, service_no, other_regiment, other_service_no, medals, enlistment_date, discharge_date, death_date, misc_info_nroh, cemetery_memorial, cemetery_memorial_ref, cemetery_memorial_country, additional_cwgc_info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
        "BuriedInBradford": "INSERT INTO BuriedInBradford (surname, forename, age, medals, date_of_birth, rank, unit, cemetary, grave_ref, info) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"
    }

    # Insert the data into the database
    if desired_table == "BradfordMemorials":
        print(f"Inserting data into {desired_table}...")
    elif desired_table == "NewspaperReferences2025":
        print(f"Inserting data into {desired_table}...")
    elif desired_table == "BiographySpreadsheet":
        print(f"Inserting data into {desired_table}...")
    elif desired_table == "RollOfHonour":
        print(f"Inserting data into {desired_table}...")
    elif desired_table == "BuriedInBradford":
        # init variables for spreadsheet filtering
        iterator = 0
        filter_data = {
                        "WW1 Burials in Bradford": {"max_rows": 5, "skip_rows": 2}
                      }
        sheet_names = ["WW1 Burials in Bradford"]

        for sheet_name in sheet_names:
            max_rows_iter = filter_data[sheet_name]["max_rows"]
            for row in sheetData[sheet_name]:
                if max_rows_iter == 0:
                    break
                if iterator < filter_data[sheet_name]["skip_rows"]:
                    iterator += 1
                    continue

                cursor.close()
                cursor = database.cursor()
                cursor.execute(insert_statements[desired_table], row)

                max_rows_iter -= 1

        print(f"Inserting data into {desired_table}...")

    return True

def detect_table(sheetData: dict) -> str:
    first_layer_keys = list(sheetData.keys())
    table_name_detection = "Unknown"
    fk = first_layer_keys[0]
    if fk == "Analytics":
        table_name_detection = "BuriedInBradford"
    elif fk == "Bradford CWGC":
        table_name_detection = "BradfordMemorials"
    elif fk == "Sheet1":
        iter = 0
        for sheet in sheetData:
            if iter == 0:
                first_row = sheetData[sheet][0]
                no_of_values = len(first_row)

                if no_of_values == 6:
                    table_name_detection = "BiographySpreadsheet"
                elif no_of_values == 23:
                    table_name_detection = "RollOfHonour"
                elif no_of_values == 11:
                    table_name_detection = "NewspaperReferences2025"
            iter += 1

    return table_name_detection

# Assigned to: ???
# This function will add a singular row to the SQL database
def singular_add_sql(dataObject: dict, databaseName: str):
    return True

# Do not edit any code below this point.
# Only edit code you have been assigned in this project.
if __name__ == "__main__":
    create_database()
    insert_to_sql(load_xlsx("Tests Data/Those buried in Bradford.xlsx"))
    exit()
