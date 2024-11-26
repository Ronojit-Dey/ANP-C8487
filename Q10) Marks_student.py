# The marks obtained by a student in 5 different subjects are input by the user. The student gets a division as per the following rules:
# Percentage above or equal to 60 - First division 
# Percentage between 50 and 59 - Second division 
# Percentage between 40 and 49 - Third division 
# Percentage less than 40 - Fail 
# Write a program to calculate the division obtained by the student. 

marks1 = float(input("Enter Marks"))
marks2 = float(input("Enter Marks"))
marks3 = float(input("Enter Marks"))
marks4 = float(input("Enter Marks"))
marks5 = float(input("Enter Marks"))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100

if percentage >= 60:
    print("First division")
elif 50 <= percentage < 60:
    print("Second division")
elif 40 <= percentage < 50:
    print("Third division")
else:
    print("Fail")


