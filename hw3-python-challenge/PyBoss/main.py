# Convert employee record into a different format
# 2018-04-29

import os
import csv
import us_state_abbrev

# Specify file path
directory = 'raw_data'
file_name = 'employee_data1.csv'
file_path = os.path.join(directory, file_name)

# Initiate variables
new_data_list = []
fieldnames = ['Emp ID', 'First Name', 'Last Name', 'DOB', 'SSN', 'State']

# Retrieve data from csv data
with open(file_path, newline = '') as file_in:
    reader = csv.DictReader(file_in, delimiter = ',')
    for row in reader:
        dictionary = {}
        dictionary['Emp ID'] = row['Emp ID']
        first, last = row['Name'].split(' ')
        dictionary['First Name'] = first
        dictionary['Last Name'] = last
        year, month, day = row['DOB'].split('-')
        dictionary['DOB'] = '/'.join([month, day, year])
        ssn_last = row['SSN'].split('-')[2]
        ssn_hidden = '***-**-' + ssn_last
        dictionary['SSN'] = ssn_hidden
        state_abbrev = us_state_abbrev.us_state_abbrev[row['State']]
        dictionary['State'] = state_abbrev
        new_data_list.append(dictionary)


