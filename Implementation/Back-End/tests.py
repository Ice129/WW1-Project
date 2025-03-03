from backend import load_xlsx, detect_table

def test_load_xlsx():
    filePath = "Tests Data/Bradford and surrounding townships Great War Roll of Honour 2025.xlsx"
    data = load_xlsx(filePath)
    for sheet in data:
        first_row = data[sheet][0]
        no_of_values = len(first_row)
        no_of_rows = len(data[sheet])

        assert no_of_values == 23
        assert no_of_rows == 15000
        print(f"Sheet: {sheet} has {len(data[sheet])} rows and {no_of_values} columns")

def test_detect_table():
    database_files = (str("Tests Data/Biography spreadsheet.xlsx"),str("Tests Data/Bradford and surrounding townships Great War Roll of Honour 2025.xlsx"),str("Tests Data/Bradford Memorials.xlsx"),str("Tests Data/Newspaper references 2025.xlsx"),str("Tests Data/Those buried in Bradford.xlsx"))
    
    for file in database_files:
        data = load_xlsx(file)
        table_name = detect_table(data)
        print(f"Detected table name: {table_name}")

    pass

if __name__ == "__main__":
    test_load_xlsx()
    test_detect_table()
    exit()
