# If the ages of Ram, Sulabh and Ajay are input by the user, write a program to determine the youngest of the three.


ram= int(input("Enter Ram's age: "))
sulabh = int(input("Enter Sulabh's age: "))
ajay = int(input("Enter Ajay's age: "))

if ram < sulabh and ram < ajay:
    print("Ram is the youngest.")
elif sulabh < ram and sulabh < ajay:
    print("Sulabh is the youngest.")
elif ajay < ram and ajay < sulabh:
    print("Ajay is the youngest.")
else:
    print("Two or more are of the same youngest age.")
