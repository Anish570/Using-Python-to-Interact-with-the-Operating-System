# Question 4
# The file_date function creates a new file in the current working directory, checks the date that
# the file was modified, and returns just the date portion of the timestamp in the format of yyyy-mm-dd. 
# Fill in the gaps to create a file called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    if not os.path.exists(filename):
        with open(filename, "w+") as file:
            pass
    # Get the file's last modification timestamp
    timestamp = os.path.getmtime(filename)
    # Convert the timestamp into a datetime object
    date = datetime.datetime.fromtimestamp(timestamp)
    # Return just the date portion in yyyy-mm-dd format
    return "{:04d}-{:02d}-{:02d}".format(date.year, date.month, date.day)

print(file_date("newfile.txt"))
