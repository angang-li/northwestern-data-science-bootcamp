# Analyze passages with simple metrics
# 2018-04-29

import os

# Specify file path
directory = 'raw_data'
file_name = 'paragraph_1.txt'
file_path = os.path.join(directory, file_name)

# Read the paragraph into a string
with open(file_path, 'r') as file_in:
    paragraph = file_in.read()
    
