# 10/03/2021
# water balance/soil database code

import openpyxl
from pathlib import Path

xlsx_file = Path('Water-Example', 'water balanace example.xlsx')
data_obj = openpyxl.load_workbook(xlsx_file)
sheet = data_obj.active

print(data_obj)