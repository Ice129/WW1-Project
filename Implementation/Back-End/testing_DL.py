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
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        self.assertEqual(Headers[1], "surname")  #The second Header should be surname

    def test_Data_Base_Header_Extraction_last(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        Headers = [description[0] for description in cursor.description]
        self.assertEqual(Headers[-1], "info")  #The last Header should be info

    def test_Data_Base_data_Extraction_1(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        self.assertEqual(Data[0][1],  "Ackrel")  #The first Surname should be Ackrel

    def test_Data_Base_data_Extraction_2(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        self.assertEqual(Data[0][2],  "William Frank")  #The first forename should be William Frank

    def test_Data_Base_data_Extraction_last_1(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        self.assertEqual(Data[-1][1],  "MacIntosh")  #The Surname of the last data entry should be MacIntosh

    def test_Data_Base_data_Extraction_last_0(self):
        database = sqlite3.connect("database.db")
        cursor = database.cursor()
        cursor.execute("SELECT * FROM BuriedInBradford")
        Data = cursor.fetchall()
        self.assertEqual(Data[-1][0],  464)  #the last data entry should be the 464th value



if __name__ == '__main__':
    unittest.main()
