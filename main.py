import csv
import random

# Open a new file in 'w'rite mode
with open('output.csv', 'w') as output_file:
    writer = csv.writer(output_file)

    # Write the header row
    writer.writerow(['Name', 'Age'])

    # Write a bunch of random data
    for name in ['John', 'Bob', 'Alice', 'Quentin', 'Mary']:
        writer.writerow([name, random.randrange(18, 28)])