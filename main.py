import math


factor = 100

while True:
    age = int(input("Please enter your age "))

    if int(age) <= 8:
        print("you should be atleast 9 to play along")
    else:
        #year=int(input("Please enter the current year ")) ## user decides year ##
        yearcurr=2020
        print("you are ", age , " years old, and the current year is",yearcurr,"\n")

        ageplus100 = int(age)+factor
        #yearplus100 = int(year)+factor ## take the year as a user input ##
        yearpluscurr100 = int(yearcurr)+factor #assuming current year is 2020
        print("in", factor, "years you will be", ageplus100, "and the year will be", yearpluscurr100,"\n")

    stop = (input("Do you wanna go again enter y to continue, and n to stop "))
    if stop == "y":
        continue
    elif stop == "n":
        break
