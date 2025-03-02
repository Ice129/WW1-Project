from backend import load_xlsx

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

if __name__ == "__main__":
    test_load_xlsx()
    exit()
