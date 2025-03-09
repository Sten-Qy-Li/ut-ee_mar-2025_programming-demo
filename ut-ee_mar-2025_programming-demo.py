""" Sample demonstration of programming skills
Submitted for admission into University of Tartu Master's in Computer Science programme """

# Import required Python packages
import pandas as pd
import openpyxl
from openpyxl import load_workbook
import numpy as np


# PART ONE OF TWO - GENERATE XLSX FILE OF RAW DATA VALUES (RANDOM)

list_wafer = []
list_testsite = []
list_volume = []
list_bin2 = []
list_bin3 = []
list_bin4 = []
list_bin5 = []
list_bin6 = []
list_bin7 = []
list_bin8 = []
list_bin9 = []
list_pass = []

for i in range(25):
    for j in range(4):
        list_wafer.append(i + 1)
        list_testsite.append(j)
        list_volume.append(250)
        list_bin2.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin3.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin4.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin5.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin6.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin7.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin8.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_bin9.append(max(0, np.random.binomial(19, 0.5, size=None) - 9))
        list_pass.append(250 - list_bin2[(4 * i) + j] - list_bin3[(4 * i) + j] 
                         - list_bin4[(4 * i) + j] - list_bin5[(4 * i) + j] 
                         - list_bin6[(4 * i) + j] - list_bin7[(4 * i) + j] 
                         - list_bin8[(4 * i) + j] - list_bin9[(4 * i) + j])

DF_DATA = {'Wafer No.': list_wafer, 'Test Site': list_testsite, 'Volume': list_volume, 
                  'Pass': list_pass, 'Bin2': list_bin2, 'Bin3': list_bin3, 'Bin4': list_bin4, 
                  'Bin5': list_bin5, 'Bin6': list_bin6, 'Bin7': list_bin7, 'Bin8': list_bin8, 
                  'Bin9': list_bin9}

DF = pd.DataFrame(data=DF_DATA)

DF.to_excel("Generated_XLSX.xlsx")


# PART TWO OF TWO - ANALYSIS OF GENERATED XLSX FILE DATA

WB = load_workbook(filename = 'Generated_XLSX.xlsx')

#https://openpyxl.readthedocs.io/en/3.1.3/simple_formulae.html
WS = WB.active

WS["A1"] = "NO."
WS["N1"] = "MAX"

for i in range(100):
    str_active_row = str(i + 2)
    str_active_cell = 'N' + str_active_row #https://docs.python.org/3/tutorial/introduction.html
    str_formulae = '=MAX(F' + str_active_row + ':M' + str_active_row + ')'
    WS[str_active_cell] = str_formulae

# WB.save('ANALYZED_XLSX.xlsx') #https://openpyxl.readthedocs.io/en/stable/tutorial.html

#https://docs.python.org/3/library/os.html
# import os
# os.system("start EXCEL.exe ANALYZED_XLSX.xlsx")
# os.system("taskkill /F /IM EXCEL.exe")

#https://openpyxl.readthedocs.io/en/stable/worksheet_tables.html
from openpyxl.worksheet.table import Table
# WB = load_workbook(filename = 'ANALYZED_XLSX.xlsx', data_only=True)
# WS = WB.active
TAB = Table(displayName="Table1", ref="A1:N101")
WS.add_table(TAB)

WB.save("ANALYZED_XLSX.xlsx")







