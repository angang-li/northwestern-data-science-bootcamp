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
candidate_number = {}
winner_vote = 0

# Read the csv file using csv.DictReader
with open(file_path, newline='') as file_in:
    csvreader = csv.DictReader(file_in, delimiter = ',')
    for row in csvreader:
        candidate = row['Candidate']
        voter_id.append(row['Voter ID'])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_number[candidate] = 1
        else:
            candidate_number[candidate] += 1

# Calculate summary data
total_votes = len(voter_id) # total number of votes
candidate_percentage = {candidate : candidate_number[candidate]/total_votes \
                        for candidate in candidates}
for item in candidate_percentage.items():
    if item[1] > winner_vote:
        winner_vote = item[1]
        winner = item[0]

# Store results to a list
results = []
results.append('Election Results')
results.append('-' * 25)
results.append(f"Total Votes: {total_votes}")
results.append('-' * 25)
for candidate in candidates:
    results.append("{}: ".format(candidate) + \
                    "{:.1%}".format(candidate_percentage[candidate]) + \
                    " ({})".format(candidate_number[candidate]))
results.append('-' * 25)
results.append(f"Winner: {winner}")
results.append('-' * 25)
