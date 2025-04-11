import unittest
import openpyxl
import sqlite3
import pandas as pd
import xlsxwriter

class MyTestCase(unittest.TestCase):



    def test_Data_Base_Header_Extraction_1(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        self.assertEqual(Headers[0], "ID")  #The first Header should be ID


    def test_Data_Base_Header_Extraction_2(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        self.assertEqual(Headers[1], "surname")  #The second Header should be surname

    def test_Data_Base_Header_Extraction_last(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        self.assertEqual(Headers[-1], "photo_incl")  #The last Header should be photo_incl

    def test_Data_Base_data_Extraction_1(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        self.assertEqual(Data[0][1],  "Abbertson")  #The first Surname should be Abberson

    def test_Data_Base_data_Extraction_2(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        self.assertEqual(Data[0][2],  "W")  #The first forename should be W

    def test_Data_Base_data_Extraction_last_1(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        self.assertEqual(Data[-1][1],  "Yates")  #The Surname of the last data entry should be Yates

    def test_Data_Base_data_Extraction_last_0(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM NewspaperReferences2025")
        Data = cursor.fetchall()
        self.assertEqual(Data[-1][0],  3629)  #the last data entry should be the 3629th value



if __name__ == '__main__':
    unittest.main()
