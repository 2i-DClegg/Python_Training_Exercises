#Task List

#Read Files

#Generate Report


##Takes a file extension and returns the contents as a concatenated string
def read_file(file_ext):
    file = open(file_ext)
    lines = ""
    for line in file:
        lines += line
    return lines    

print(read_file("test.txt"))