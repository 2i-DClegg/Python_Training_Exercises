#Task List

#Read Files

#Generate Report


##Takes a file extension and return a array of strings
def read_file(file_ext):
    file = open(file_ext)
    lines = []
    for line in file:
        lines.append(line.replace("\n", ""))
    file.close()
    return lines

    
# Function takses 
def text_error_check(text_lines):
    if text_lines is None:
        raise Exception("Missing arguments -> text_lines")
    error_lines = []
    critical_lines = []
    for line in text_lines:
        if "ERROR" in line:
            error_lines.append(line)
        if "CRITICAL" in line:
            critical_lines.append(line)
    return error_lines, critical_lines


    

print(read_file("test.txt"))