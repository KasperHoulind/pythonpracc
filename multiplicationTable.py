for i in range(1,11): #goes up to 11  but does not includes 11
    for j in range(1,11):
        print(i*j, end="\t") #sets the tab char,to create a table format, switch lines when reaching end of display range.
    print('') #sets new line after each set of 10 and gives a cleaner output.