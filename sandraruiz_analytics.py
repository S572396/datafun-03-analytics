"""This module is for project 3 to practice creating virtual environment, write and process data by 
    working with text, csv, excel, and json
"""
# Library imports
import math
import statistics
import pathlib
import os
import time
import csv
from collections import Counter
import pandas 


def main():
    '''Wokring with data with modules and functions.'''
    #example working with text data by word_counter using collections
    #example value and statistics using pandas
    #example working with csv data for row output and if else logic
    #example with with xcel data for sum of Rent prices using pandas
    #example with json data with logic to catch errors
   
    
# Define function 1: text data example 1
text = ('This is a sample that I am going to type several words '
        'I want to see the count '
        'I will type this is and this is and not this is a few times')

word_counter = Counter(text.split())

for word, count in sorted(word_counter.items()):
    print(f'{word:<12} {count}')

try:
    from collections import Counter
    print("collections module is available.")
except ImportError:
    print("collections module is not available.")

#function of a list example 2
import pandas as pd

values = pd.Series([100, 15, 22, 79, 45, 17, 99, 52])

import pandas as pd

values = pd.Series([100, 15, 22, 79, 45, 17, 99, 52])

print(values)
print(values.describe())
statistics_summary = values.describe()
print("\nSummary Statistics:")
print(statistics_summary)

# file path for statistics results
output_text_file_path = 'statistics.txt'

with open(output_text_file_path, 'w') as text_file:
    text_file.write("Summary Statistics:\n")
    text_file.write(statistics_summary.to_string())

print(f"\nSummary statistics saved to {output_text_file_path}")

#define function 2, csv data
import csv
import logging
import os

# CSV file path using
csv_file_path = r'C:\Users\19564\OneDrive\Rent List.csv'

if not os.path.exists(csv_file_path):
    print(f"File not found: {csv_file_path}")
else:
    
    with open(csv_file_path, 'r') as file:

        csvreader = csv.reader(file)

        header = next(csvreader)
        print(header)

        rows = []
        for row in csvreader:
            rows.append(row)

            print(f"Row: {row}")

output_text_file_path = 'row_data.txt'

# To save row output
with open(output_text_file_path, 'w') as text_file:
    for row in rows:
        print(f"Row: {row}", file=text_file)

print(f"Print output saved to {output_text_file_path}")

# define function 3 with excel data
import pandas as pd

# Using Excel file
xlsx_file_path = r'C:\Users\19564\OneDrive\Rent List.xlsx'

df = pd.read_excel(xlsx_file_path)

column_name = 'Price'
column_sum = df[column_name].sum()
print(f"Sum of column {column_name}: {column_sum}")
output_text_file_path = 'output.txt'

# Output for the text file
with open(output_text_file_path, 'w') as text_file:
    print(f"Sum of column {column_name}: {column_sum}", file=text_file)

print(f"Print output saved to {output_text_file_path}")

#define function 4, json data
import requests 
import json
import sys

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

json_data_path = 'C:\\Users\\19564\\datafun-03-analytics\\Rent.json'

try:
    with open(json_data_path, 'r') as file:
        content = file.read()
        if not content:
            raise ValueError('The file is empty')

        json_data = json.loads(content)
        save_json(json_data, 'output.json')
        print('JSON data saved successfully.')

        # Save print output to json.txt
        with open('json.txt', 'w') as output_file:
            sys.stdout = output_file
            print('JSON data saved successfully.')
            sys.stdout = sys.__stdout__
except FileNotFoundError:
    print(f'Failed to find the file: {json_data_path}')

if __name__ == '__main__':
    main()

