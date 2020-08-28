file = open("C:\\PythonProjects\\pythonpracc\\real.txt","r")


sWord = input("Enter a word to search for, the serach funcition is case senstive ")
for line in file:
    if sWord in line:
        print(line)
    else:
        pass
        #print("nothing found")

file.close()