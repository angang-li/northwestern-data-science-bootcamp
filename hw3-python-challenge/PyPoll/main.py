# Analyze election results
# 2018-04-28

import os
import csv

# Assign file path of election data
directory = 'raw_data'
file_name = 'election_data_1.csv'
file_path = os.path.join(directory, file_name)

# Preallocate variables
keys = ['Candidate', 'Number of Votes', 'Percentage of Votes']
voter_id = []
candidates = []
dictionary = {}

# Read the csv file using csv.DictReader
with open(file_path, newline='') as file_in:
    csvreader = csv.DictReader(file_in, delimiter = ',')
    for row in csvreader:
        candidate = row['Candidate']
        voter_id.append(row['Voter ID'])
        if candidate not in candidates:
            candidates.append(candidate)
            dictionary[candidate] = 1
        else:
            dictionary[candidate] += 1

