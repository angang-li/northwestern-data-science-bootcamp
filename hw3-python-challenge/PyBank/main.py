# Analyze the financial record
# 2018-04-28

# Import modules
import os
import csv

# Specify file path
file_path = os.path.join(directory, file_name)

# Initialize variables
month_year_list = []
revenue_list = []
tot_revenue = 0
tot_change = 0
change_max = ['', 0]
change_min = ['', 0]

# Read csv data to gather date and revenue data
with open(file_path, newline = '') as file_in:
    csvreader = csv.reader(file_in, delimiter = ',')
    next(csvreader, None)
    for row in csvreader:
        month_year = row[0]
        revenue = float(row[1])
        month_year_list.append(month_year)
        revenue_list.append(revenue)
        tot_revenue += revenue
