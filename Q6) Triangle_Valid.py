# Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered by the user.
# A triangle is valid if the sum of all the three angles is equal to 180 degrees.

angle1 = float(input())
angle2 = float(input())
angle3 = float(input())

if angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
    print("The triangle is valid.")
    
else:
    print("The triangle is not valid.")


