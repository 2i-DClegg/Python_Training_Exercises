#Task List

#Read Files

#Generate Report


##Takes a file extension and return an array of lines
def read_file(file_ext):
    file = open(file_ext)
    lines = []
    for line in file:
        lines.append(line)
    return lines  

    
##Function takes an array of strings and a keyword, and filters the strings that contain the keyword
def line_keyword_check(text_lines, keyword):
    if text_lines is None:
        raise Exception("Missing arguments -> text_lines")
    if keyword is None:
        raise Exception("Missing arguments -> keyword")
    checked_lines = []
    for line in text_lines:
        if keyword in line:
            checked_lines.append(line)
    return checked_lines

print(line_keyword_check(read_file("test.txt"), "ERROR"))