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


#Takes a file extension, reads the contents, and writes the Error and Critical Lines to a .txt file
def generate_report(log_file_ext):
    log_file_contents = read_file(log_file_ext)
    report_file_name = "./reports/" + log_file_ext.replace(".txt", "_error_report.txt")
    
    report_file = open(report_file_name, "a")

    error_lines, critical_lines = text_error_check(log_file_contents)
    print("GENERATING REPORT FOR: " + log_file_ext)
    report_file.write("GENERATING REPORT FOR: " + log_file_ext +"\n")
    print("===================")
    report_file.write("===================\n")
    print("Total Error Messages: ", len(error_lines))
    report_file.write(f"Total Error Messages: {len(error_lines)}\n")
    for error_line in error_lines:
        print(error_line)
        report_file.write(f"{error_line}\n")
    print("===================")
    report_file.write("===================\n")
    print("Total Critical Messages: ", len(critical_lines))
    report_file.write(f"Total Critical Messages: {len(critical_lines)}\n")
    for critical_line in critical_lines:
        print(critical_line)
        report_file.write(f"{critical_line}\n")

    report_file.write("End of report\n")
    report_file.write("===================\n")
    report_file.close()
    

generate_report("test.txt")