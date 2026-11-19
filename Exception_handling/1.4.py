def read_file_safely(filename):
    try:
        file = open(filename, "r")
        date = file.read()
        file.close()
        return date
    except FileNotFoundError:
     return "file not found"
 
print(read_file_safely("Exception_handling/python.py"))
        