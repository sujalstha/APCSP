# 10/03/2021
# water balance/soil database code

import pandas as pd

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
waterBalance = pd.read_csv('water balanace .csv', usecols=[7])

print(waterBalance)

# print(waterBalance["Allowable Depletion balance (ADB)"])
