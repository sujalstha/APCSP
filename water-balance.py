# 10/03/2021
# water balance/soil database code

import pandas as pd

colm = ['Day', "Rainfall",
        "Irrigation",
        "Etc",
        "Soil moisture",
        "Total available water",
        "Daily Balance (DB)",
        "Allowable Depletion balance (ADB)"]

C_1 = 0.90
F_1 = 15
H_1 = 0.21
J_1 = 0.09


def Calibrate(colm_e):
    formula = F_1 * (colm_e - J_1) * 0.5
    return formula


def H_Colm_val(prev_H, G_row):
    formula = prev_H + G_row
    return formula


# ADB first value formula : 0.3= F_1*(E4-J_1)*0.5
# 7 col, 34 row
wB = pd.read_csv('water balanace .csv', usecols=colm)

DB_col = wB["Daily Balance (DB)"]
ADB_col = wB["Allowable Depletion balance (ADB)"]
Soil_col = wB["Soil moisture"]

DB_list = []
ADB_list = []
Soil_moisture_list = []

for x in DB_col:
    DB_list.append(x)

for x in ADB_col:
    ADB_list.append(x)

for x in Soil_col:
    Soil_moisture_list.append(x)

del DB_list[0]
del Soil_moisture_list[0]
del ADB_list[0]

for index, value in enumerate(ADB_list):
    print(index, value)

print('')
for index, value in enumerate(DB_list):
    print(index, value)

