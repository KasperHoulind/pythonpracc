import math

while True:
    number = int(input("Enter a number "))

    if int(number%2)==0:
        print("your number is even, This is the number you enterede: ", number, "\n")
    else:
        print("your number is odd, This is the number you enterede: ", number, "\n")

    stop = (input("Do you wanna go again enter y to continue, and n to stop "))
    if stop == "y":
        continue
    elif stop == "n":
        break