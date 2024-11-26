# Any character is entered by the user; write a program to determine whether the 
# character entered is a capital letter, a small case letter, a digit or a special symbol.
# The following table shows the range of ASCII values for various characters

char = input()

if len(char) != 1:
    print("Please enter only one character.")
elif 'A' <= char <= 'Z':
    print("Capital letter")
elif 'a' <= char <= 'z':
    print("Small case letter")
elif '0' <= char <= '9':
    print("Digit")
else:
    print("Special symbol")




