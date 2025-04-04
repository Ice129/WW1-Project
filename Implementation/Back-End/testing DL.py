import unittest
import openpyxl
import sqlite3
import pandas as pd
import xlsxwriter

class MyTestCase(unittest.TestCase):
    database = sqlite3.connect("database.db")
    cursor = database.cursor()
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def DLNewspaperReferences2025():
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        HeadersWithData = {}
        for num in range(len(Headers) - 1):
            HeadersWithData = {**HeadersWithData, Headers[num + 1]: [d[num + 1] for d in Data]}
        df = pd.DataFrame(HeadersWithData)
        writer = pd.ExcelWriter("NewspaperReferences2025.xlsx", engine="xlsxwriter")
        df.to_excel(writer, sheet_name="sheet1", index=False)
        workbook = writer.book
        worksheet = writer.sheets["sheet1"]
        worksheet.autofit()
        workbook.close()


if __name__ == '__main__':
    unittest.main()
