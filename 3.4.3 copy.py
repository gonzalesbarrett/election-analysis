import os
import csv

# Create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join('Analysis/election_analysis.txt')

# Using the open() function with the"w" mode we will write data to the right
with open(file_to_save, "w") as txt_file:

# Write some data to the file
    txt_file.write("Counties in the election\n---------------------------------\nArapahoe\nDenever\nJefferson")

# Close the file
txt_file.close()