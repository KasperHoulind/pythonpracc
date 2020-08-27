import math

age = int(input("Please enter your age "))
factor = 100

if int(age) <= 8:
    print( "you should be atleast 9 to play along")
else:
    year =int(input("Please enter the current year "))
    print("you are ", age , " years old, and the current year is",year)

    ageplus100 = int(age)+factor
    yearplus100 = int(year)+factor
    print("in", factor, "years you will be", ageplus100, "and the year will be", yearplus100)








