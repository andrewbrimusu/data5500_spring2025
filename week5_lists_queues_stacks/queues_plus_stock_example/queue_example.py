"""
This program reads lines from a file, stores up to 6 of them in a queue,
and computes the average of those 6 values each time the queue is full.
Then it discards the oldest value to make room for the next one.
This approach is memory-efficient because it only keeps the necessary data
(6 values) at any time.
"""

import os

# Get the current directory of this file
curr_dir = os.path.dirname(__file__)

# Replace "numbers.txt" with your actual filename
data_file = os.path.join(curr_dir, "AAPL.txt")
file = open(data_file, "r")

# We'll keep at most 6 values in our list (acting as a queue)
queue_size = 6
values = []

# Read the first line
line = file.readline()

while line:
    # Convert the line to a float (assuming the file has numeric data)
    val = float(line.strip())
    values.append(val)

    # Once we have 6 items, compute the average
    if len(values) == queue_size:
        avg = sum(values) / len(values)
        print("Current queue:", values)
        print("Average of these 6 values:", avg)
        print("----------")
        
        # Remove the oldest item
        values.pop(0)
    
    # Read the next line
    line = file.readline()

file.close()

# If the file has fewer than 6 lines total,
# you might want to calculate averages for
# the remaining lines here, or just ignore them.
# For now, we'll do nothing special.

print("Done processing file.")
input("Press Enter to exit...")
