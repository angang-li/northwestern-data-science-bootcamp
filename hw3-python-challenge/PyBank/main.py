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

# Loop through the list to calculate summary data
    tot_month = len(month_year_list)
    for i in range(1, len(month_year_list)):
        change = revenue_list[i] - revenue_list[i-1]
        tot_change += change
        if change > change_max[1]:
            change_max = [month_year_list[i], change]
        if change < change_min[1]:
            change_min = [month_year_list[i], change]
    change_average = tot_change / tot_month

