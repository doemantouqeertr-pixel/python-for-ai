





#------------IMPORT PACKAGES-------------:-

# using packages
'''
Python packages add functionality to your 
programs. There are two types of packages:
> built in : come with python
> external : need to install
'''

# understanding terminology
'''
> module : a single python file
> package : a folder containing multiple module
> funtion : a reusable block of code
> class : a blueprint for creating objects
'''








#======================================================


# import pattern

import math #import whole  module
math.sqrt(16)

from math import sqrt, pi #import specific item
sqrt(16)


#======================================================


# Built-in modules

import random # (import entire module)

number = random.randint(2, 20) # (use module functions)
choice = random.choice(["ema","jade","zay"])


#======================================================











# Common built-in modules

# date and time:
import datetime
today = datetime.date.today()
print(today)

# operating system:
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data:
import json
data = {"name": "william" , "age": 18}
json_string = json.dumps(data)


#======================================================


# Import with alias

import pandas as pd

data = {
 "name" : {"Eman" , "Zayden" , "jade"},
 "age" : {"17", "18", "19" },
 "city" : {"Nyc", "Paris", "Tokyo"}
 }

df = pd.DataFrame(data)


#======================================================


# Import everything (avoid this!!!)
from math import *


#======================================================


# Installing packages
'''
External packages need installation
'''
# Install a package:
'''
pip install requests
'''
# Install a specific version:
'''
pip install requests == 2.28.0
'''
# Install multiple packages:
'''
pip install pandas numpy matplotlib
'''


#======================================================



# SHARING YOUR PROJECT : requirements.txt
'''
on sharing your projects ppl do need to know which 
packages to install. The standard way is using a 
requirements.txt file:
'''

# creating requirements.txt
'''
list all your project's packages:
pip freeze > requirements.txt
'''

# installing from requirements.txt
'''
when someone gets your project, they run:
pip install -r requirements.txt
'''