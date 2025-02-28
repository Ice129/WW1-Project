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

# Assigned to: ???
# This function will load a CSV file from a given location and return it as a dictionary
def load_csv(fileLocation: str):
    return {}

# Assigned to: ???
# This function will instantiate the databases as well as their columns for the next function, insert_to_sql()
def create_database():
    return True

# Assigned to: ???
# This function will call the load_csv() on all of the csv files in the directory
# It will then convert their returned values into the created SQL databases in create_database()
def insert_to_sql():
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