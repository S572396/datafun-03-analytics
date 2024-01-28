# datafun-03-analytics
##create project virtual environment in the .venv folder
'''
py -m venv .venv
.venv\Scripts\Activate
py -m pip install -r requirments.txt
'''
##git add and commit
'''
git add .
git commit -m "add .gitignore, cmds to README"
git push origin main

## '''Wokring with data with modules and functions.'''
    1#example working with text data by word_counter using collections, result on print only
    2#example value and statistics using pandas,result on statistics.txt and print
    3#example working with csv data for row output and if else logic, result on row_data.txt and print
    4#example with with xcel data for sum of Rent prices using pandas,result on output.txt and print
    5#example with json data with logic to catch errors,result on json.txt and print statement
    
## Installs Used
    pip upgrade
    pip freeze
    pip install pyxl (for Excel)

# Library imports
import math
import statistics
import pathlib
import os
import time
import csv
from collections import Counter
import pandas 
'''