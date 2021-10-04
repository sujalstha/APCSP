# 10/03/2021
# water balance/soil database code

import pandas as pd

C_1 = 0.90
F_1 = 15
H_1 = 0.21

waterBalance = pd.read_csv('water balanace .csv', usecols=[0])

print(waterBalance)

#print(waterBalance["Allowable Depletion balance (ADB)"])