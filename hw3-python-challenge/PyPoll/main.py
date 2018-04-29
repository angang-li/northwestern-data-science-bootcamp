# Analyze election results
# 2018-04-28

# Define a function that analyzes election results
def poll_results(directory, file_name):

    """
    Analyze and print election results

    inputs:
        directory - str, folder of the csv file
        file_name - str, name of the csv file including extension
    outputs:
        total_votes - int, total number of votes
        candidate_number - dict, candicates and their corresponding vote number
        candidate_percentage - dict, candicates and their corresponding vote percentage
        winner - str, name of the winner of the election based on popular vote
    """

    import os
    import csv

    # Assign file path of election data
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

    # Print results to terminal
    for line in results:
        print(line)

    # Save results to a text file
    output_file_path = file_name.split('.')[0] + '_out.txt'
    with open(output_file_path, 'w') as file_out:
        for line in results:
            file_out.write(line + '\n')

# Analyze a specific csv file using the defined function
directory = 'raw_data'
file_name = 'election_data_1.csv'
poll_results(directory, file_name)

# Analyze a specific csv file using the defined function
directory = 'raw_data'
file_name = 'election_data_2.csv'
poll_results(directory, file_name)

