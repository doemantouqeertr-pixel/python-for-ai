

import os
import pandas as pd
import json


# CHECKING WHETHER THE PATH IS RIGHT


print("current directory:" , os.getcwd())
data_path = "data/study_log.csv"

if os.path.exists(data_path):
    print(f"Found the path {data_path}")
else:
    print(f"No, couldn't find the {data_path}")

# output
'''
Found the path data/study_log.csv
'''




#  READING THE CSV FILE - NEEDS EXACT PATH

with open(f"{data_path}", "r") as file:
    content = file.read()
print(content)

# output
'''

date, subject, study_hours, practical_hours

2026-10-25, python, 3, 2
2026-10-26, maths, 2, 1
2026-10-27, maths, 2, 2
2026-10-28, python, 2, 3
2026-10-29, python, 3, 1
2026-10-30, maths, 3, 2

'''




# USING PANDAS

from helpers import load_log

ef = load_log(data_path)



print("-" * 56)
print("STUDY DATA FOR LAST WEEK")
print("-" * 56)
print(ef)
print("-" * 56)

n_rows = ef.shape[0]
n_columns = ef.shape[1]
print(f"\n SHAPE: {n_rows} rows, {n_columns} columns")

# output
'''
--------------------------------------------------------
STUDY DATA FOR LAST WEEK
--------------------------------------------------------
          date  subject   study_hours   practical_hours
0  2026-10-25   python             3                 2
1  2026-10-26    maths             2                 1
2  2026-10-27    maths             2                 2
3  2026-10-28   python             2                 3
4  2026-10-29   python             3                 1
5  2026-10-30    maths             3                 2
--------------------------------------------------------

 SHAPE: 6 rows, 4 columns
 '''










# NOW CALCULATING TOTAL STUDY HOURS AND PRACTICAL HOURS

print("-" * 70)
print("STUDY DATA FOR LAST WEEK")
print("-" * 70)

from helpers import add_total_hours
ef = add_total_hours(ef)
print(ef)

print("-" * 70)

# output
'''
----------------------------------------------------------------------
STUDY DATA FOR LAST WEEK
----------------------------------------------------------------------
          date  subject   study_hours   practical_hours  total_hours
0  2026-10-25   python             3                 2            5
1  2026-10-26    maths             2                 1            3
2  2026-10-27    maths             2                 2            4
3  2026-10-28   python             2                 3            5
4  2026-10-29   python             3                 1            4
5  2026-10-30    maths             3                 2            5
----------------------------------------------------------------------
'''





























# CREATE OUTPUT DIRECTORY

os.makedirs('output', exist_ok=True)







# SAVE AS DIFFERENT FORMATS:


# 1. JSON format (good for web APIs)
ef.to_json('output/study_log.json', orient= 'records', indent=2)
# 2. Excel format (good for sharing)
ef.to_excel('output/study_log.xlsx', index=False)
# 3. Updated CSV (with our new total column)
ef.to_csv('output/study_log_with_totals.csv', index= False)























# LOADING DIFFERENT FILE TYPES

# CSV
ef = pd.read_csv(data_path)

# JSON
ef = pd.read_json('output/study_log.json')
# or for simple json
with open('output/study_log.json' , 'r') as f:
    data = json.load(f)

# EXCEL
ef = pd.read_excel('output/study_log.xlsx')

# TEXT FILES
with open('output/study_log.txt', 'w') as f:
    f.write(ef.to_string(index=False))

with open('output/study_log.txt', 'r') as f:
    text = f.read()

print(text)

