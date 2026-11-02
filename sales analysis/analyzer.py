




'''
GOING DOWN INTO SUBFOLDERS : Use '/' for files, '.' for imports
GOING UP TO PARENT FOLDERS : Use '../' for files, add to sys.path for imports
SAME FOLDER: just use the file name

'''




import os

# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "data/sales.csv"    # '/' indicates the files
if os.path.exists(data_path):
    print(f"Found {data_path}")
else: 
    print(f"Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# Found data/sales.csv


#=============================================================================



# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "output/report.json"    # '/' indicates the files
if os.path.exists(data_path):
    print(f"Found {data_path}")
else: 
    print(f"Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# Found output/report.json



#=============================================================================




# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "../sales analysis/data"    
if os.path.exists(data_path):
    print(f"Found {data_path}")
else: 
    print(f"Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# Found ../sales analysis/data



#=============================================================================



# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "../data/paris_weather.csv"   
if os.path.exists(data_path):
    print(f"Found {data_path}")
else: 
    print(f"Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# Found ../data/paris_weather.csv







#=============================================================================





# Check if we're in the right place
print("Current directory:", os.getcwd())

# Check if our data file exists
data_path = "../../python-for-ai/.venv"    
if os.path.exists(data_path):
    print(f"Found {data_path}")
else: 
    print(f"Cannot find {data_path}")
    print("Make sure you're running from the sales-analysis folder!")

# Found ../../python-for-ai/.venv



#=============================================================================





data_path = "../sales analysis/output/report.json"

print("current dir-", os.getcwd())

if os.path.exists(data_path):
    print(f"yes this {data_path} exists")

else:
    print(f"no that {data_path} doesnt exist")

# yes this ../sales analysis/output/report.json exists



#=============================================================================




data_path = "../../python-for-ai/sales analysis/output/report.json"

print("current dir-", os.getcwd())

if os.path.exists(data_path):
    print(f"yes this {data_path} exists")

else:
    print(f"no that {data_path} doesnt exist")

# yes this ../../python-for-ai/sales analysis/output/report.json exists



#=============================================================================





data_path = "../../../coding/python-for-ai/sales analysis/output/report.json"

print("current dir-", os.getcwd())

if os.path.exists(data_path):
    print(f"yes this {data_path} exists")

else:
    print(f"no that {data_path} doesnt exist")

# yes this ../../../coding/python-for-ai/sales analysis/output/report.json exists



#===============================================================================










''' 
FILES VS MODULES:
-----------------

Python handles regular files and Python modules differently:

REGULAR FILES ( CSV, TXT, JSON):
- Use open() or file-reading functions
- Need the exact path from your current directory
- Use forward slashes: data/sales.csv

'''


#  READING A CSV FILE - NEEDS EXACT PATH

with open("data/sales.csv", "r") as file:
    content = file.read()
print(content)

'''
(out put)

date,product,quality,price

2024-01-01,Laptop,2,1999.98
2024-01-01,Mouse,5,29.99
2024-01-02,Keyboard,3,119.85
2024-01-02,Monitor,1,299.995
2024-01-03,Laptop,1,999.99
2024-01-03,Mouse,10,59.98
2024-01-04,Keyboard,2,79.99
2024-01-05,Monitor,2,599.99

'''







# FILES IN AI PROJECTS

'''
When working with python for AI, we work with data files.
They might come as:

- CSV FILES: Spreadsheet data from excel or databases.
- JSON FILES - API responses and conofiguration data.
- XML FILES - Structured data from various system.
- TEXT FILES - Raw text for processing.
- PARQUET FILES - Efficient data storage format.

'''




# COMMON LIBRARIES FOR FILES

'''
Each file type has specialized libraries:

CSV FILES:
- PANDAS : Best for data analysis 
- CSV MODULE : Built in, for simple operations

JSON FILES:
- JSON MODULE : Built-in, handles all JSON operations
- PANDAS : Can read/write JSON with DataFrames

OTHER FORMATS:
- xml.etree : Built-in XML parsing
- openpyxl : Excel files (.xlsx)
- PyPDF2 : PDF files

'''


# ----------------------------------------------------------------------------


# WORKING WITH OUR SALES DATA


import pandas as pd
import json
import os

df = pd.read_csv("data/sales.csv")

print("-"*43)
print("CSV DATA:")
print("-"*43)
print(df)
print("-"*43)


dd = df.shape[0] 
dg = df.shape[1]
print(f"\nSHAPE : {dd} rows , {dg} columns")


# OUTPUT:
'''
-------------------------------------------
CSV DATA:
-------------------------------------------
         date   product  quantity     price
0  2024-01-01    Laptop         2  1999.980
1  2024-01-01     Mouse         5    29.990
2  2024-01-02  Keyboard         3   119.850
3  2024-01-02   Monitor         1   299.995
4  2024-01-03    Laptop         1   999.990
5  2024-01-03     Mouse        10    59.980
6  2024-01-04  Keyboard         2    79.990
7  2024-01-05   Monitor         2   599.990
-------------------------------------------

SHAPE : 8 rows , 4 columns

'''









# QUICK OPERATION: CALCULATE TOTAL FOR EACH ROW

df['total'] = df['quantity'] * df['price']
print("\nWith totals:")
print(df)

# OUTPUT:
'''
With totals:
         date   product  quantity     price     total
0  2024-01-01    Laptop         2  1999.980  3999.960
1  2024-01-01     Mouse         5    29.990   149.950
2  2024-01-02  Keyboard         3   119.850   359.550
3  2024-01-02   Monitor         1   299.995   299.995
4  2024-01-03    Laptop         1   999.990   999.990
5  2024-01-03     Mouse        10    59.980   599.800
6  2024-01-04  Keyboard         2    79.990   159.980
7  2024-01-05   Monitor         2   599.990  1199.980

'''

# CREATE OUTPUT DIRECTORY

os.makedirs('output', exist_ok= True)











# SAVE AS DIFFERENT FORMATS:

# 1. JSON format (good for web APIs)
df.to_json('output/sales_data.json', orient= 'records', indent=2)
# 2. Excel format (good for sharing)
df.to_excel('output/sales_data.xlsx', index=False)
# 3. Updated CSV (with our new total column)
df.to_csv('output/sales_with_totals.csv', index= False)


print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")

# OUTPUT:
'''
Files saved:
- output/sales_data.json
- output/sales_data.xlsx
- output/sales_with_totals.csv
'''








# ----------------------------------------------------------------------------------

# LOADING DIFFERENT FILE TYPES

# CSV
df = pd.read_csv('data/sales.csv')

# JSON
df = pd.read_json('output/sales_data.json')
# or for simple json
with open('output/sales_data.json' , 'r') as f:
    data = json.load(f)

# EXCEL
df = pd.read_excel('output/sales_data.xlsx')

# TEXT FILES
with open('output/sales.txt', 'w') as f:
    f.write(df.to_string(index=False))

with open('output/sales.txt', 'r') as f:
    text = f.read()

print(text)

