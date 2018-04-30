# Analyze passages with simple metrics
# 2018-04-29

import os
import re

# Specify file path
directory = 'raw_data'
file_name = 'paragraph_1.txt'
file_path = os.path.join(directory, file_name)

# Read the paragraph into a string
with open(file_path, 'r') as file_in:
    paragraph = file_in.read()

# Read paragraph into a list of words
sentences_rough = paragraph.strip().split('. ')
words_rough = paragraph.strip().split(' ')
words_clean = []
for word_rough in words_rough:
    word_clean = word_rough.strip().strip('(),.!?;:{}[]><').lower()
    if len(word_clean) > 0:
        words_clean.append(word_clean)

# Calculate total number of letters
letters_total = 0
for word in words_clean:
    letters_total += len(word)

# Calculate metrics
word_count = len(words_clean)
sentence_count = len(sentences_rough)
average_sentence_length = float(word_count) / sentence_count
average_letter_count = float(letters_total) / word_count

# Print results to terminal
line1 = "Paragraph Analysis"
line2 = "-" * 25
line3 = f"Approximate Word Count: {word_count}"
line4 = f"Approximate Sentence Count: {sentence_count}"
line5 = f"Average Letter Count: {average_letter_count}"
line6 = f"Average Sentence Length: {average_sentence_length}"
results = [line1, line2, line3, line4, line5, line6]
for line in results:
    print(line)

# Write results to a text file
output_file_path = file_name.split('.')[0] + '_output.txt'
with open(output_file_path, 'w', newline = '') as file_out:
    for line in results:
        file_out.write(line + '\n')
