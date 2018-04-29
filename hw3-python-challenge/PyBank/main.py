# Analyze the financial record
# 2018-04-28

# Define a function that analyzes financial record
def main(directory, file_name):

    """
    input: 
        directory - str, folder of the csv file
        file_name - str, name of the csv file including extension
    output:
        tot_month - int, total number of months included in the dataset
        tot_revenue - float, total amount of revenue gained over the entire period
        change_average - float, average change in revenue between months over the entire period
        change_max - list, greatest increase in revenue (date and amount) over the entire period
        change_min - list, greatest decrease in revenue (date and amount) over the entire period
    """

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

    # Store summary data in list
    line1 = 'Financial Analysis'
    line2 = '-' * 30
    line3 = 'Total Months: ' + str(tot_month)
    line4 = 'Total Revenue: $' + str(round(tot_revenue))
    line5 = 'Average Revenue Change: $' + str(round(change_average))
    line6 = 'Greatest Increase in Revenue: ' + change_max[0] + ' ($' + str(round(change_max[1])) + ')'
    line7 = 'Greatest Decrease in Revenue: ' + change_min[0] + ' ($' + str(round(change_min[1])) + ')'
    summary = []
    summary.extend([line1, line2, line3, line4, line5, line6, line7])

    # Report summary data in terminal
    print('')
    print(file_name)
    for line in summary:
        print(line)
    print('')

    # Write summary data into a text file
    output_file_path = file_name.split('.')[0] + '_output.txt'
    with open(output_file_path, 'w') as file_out:
        for line in summary:
            file_out.write(line + '\n')

