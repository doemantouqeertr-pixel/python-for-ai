



with open("data/sales.csv") as file:
    content = file.read()
print(content)



import pandas as pd
import json
import os
m = pd.read_csv("data/sales.csv")
print("-"*43)
print("CSV DATA:")
print("-"*43)
print(m)
print("-"*43)

