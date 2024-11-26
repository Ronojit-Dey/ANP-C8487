# Any year is input by the user.
# Write a program to determine whether the year is a leap year or not.

year = int(input())

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


