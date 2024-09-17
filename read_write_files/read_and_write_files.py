
#  using  open_use_close method to read and write 
file = open("./sample.txt")
print(file.readline())
print(file.readline())
print(file.read())

file.close()

# using with statement to automatically close the file

with open("./sample.txt") as file:
    print(file.readline())
    print(file.readline())
    print(file.read())

with open("./writetest.txt","w") as file:
    file.write("This is a test file.\n")
    file.write("This is another line.\n")

with open("./sample.txt") as file:
    for line in file.readlines():
        print(line.strip().upper())