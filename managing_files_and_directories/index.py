import os

filename = "./sample.txt"
# creating file using python 
with open(filename,"w") as file:
    pass

with open(filename,"w") as file:
    file.write("Hello, this is a sample text file. We will be using this file to check it's various things such as size, last modified date etc.\n")

# getting the size of the file
print("size of the {} is: {}".format(filename,os.path.getsize(filename)))

# getting the last modified date of the file on timestamp format
print("last modified date {}".format(os.path.getmtime(filename)))

# getting the last modified date of the file on readable format datetime
import datetime
timestamp = os.path.getmtime(filename)
datetimeformat  = datetime.datetime.fromtimestamp(timestamp)
print("{} modified date in date-time format is {}".format(filename,datetimeformat))

#  modified date in yyyy-mm-dd format

datetimeformat_yyyy_mm_dd = datetimeformat.strftime("%Y-%m-%d")
print("{} modified date in yyyy-mm-dd format is {}".format(filename,datetimeformat_yyyy_mm_dd))


print("do i have {} here: {}".format(filename,os.path.exists(filename)))

#  Working with directory 



dir = "testfolder"
os.mkdir(dir)
print("{} is a directory: {}".format(dir,os.path.isdir(dir)))
os.chdir(dir)

def new_dir_and_file(dir,newdir_inside_dir, filename_in_dir):
  # Before creating a new dir, check to see if it already exists
  if os.path.isdir(newdir_inside_dir) == False:
    os.mkdir(newdir_inside_dir)

  # Create the new file 
  with open (filename_in_dir,"w+") as file:
    pass

  # Return the list of files in the new newdir_inside_dir
  os.chdir("../")
  return os.listdir(dir)

print(new_dir_and_file(dir,"PythonPrograms", "script.py"))


# Deleting the directory and its contents
os.mkdir("dirtobedeteletd")
os.rmdir("dirtobedeteletd")