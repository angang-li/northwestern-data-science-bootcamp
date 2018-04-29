# Convert employee record into a different format
# 2018-04-29

# Define a function that re-format employee record
def main(directory, file_name):

    """
    input: 
        directory - str, folder of the csv file
        file_name - str, name of the csv file including extension
    output:
        new_data_list - list, list of dictionaries that contain 
                        re-formatted record
    """

    import os
    import csv
    import us_state_abbrev

    # Specify file path
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

    # Specify output file path
    output_file_path = file_name.split('.')[0] + '_out.csv'

    # Export output data to csv file
    with open(output_file_path, 'w', newline='') as file_out:
        writer = csv.DictWriter(file_out, fieldnames = fieldnames)
        writer.writeheader()
        writer.writerows(new_data_list)

    # Print output data to terminal
    for line in new_data_list:
        print(f"{line['Emp ID']}, {line['First Name']}, {line['Last Name']}, \
{line['DOB']}, {line['SSN']}, {line['State']}")

# Analyze test record using the defined function
directory = 'raw_data'
file_name = 'employee_data1.csv'
main(directory, file_name)

# Analyze test record using the defined function
directory = 'raw_data'
file_name = 'employee_data2.csv'
main(directory, file_name)