try:
    file = open('sample.txt', 'r')
    file_contents = file.readlines()
    print("Reading file contents:")
    for i, txt in enumerate(file_contents):
        print("Line", i+1, ":", txt)
    file.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")