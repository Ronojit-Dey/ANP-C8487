# Write a program to calculate the monthly telephone bills as per the following rule: 
# Minimum Rs. 200 for upto 100 calls. 
# Plus Rs. 0.60 per call for next 50 calls. 
# Plus Rs. 0.50 per call for next 50 calls. 
# Plus Rs. 0.40 per call for any call beyond 200 calls. 


calls = int(input())

if calls <= 100:
    bill = 200
elif calls <= 150:
    bill = 200 + (calls - 100) * 0.60
elif calls <= 200:
    bill = 200 + 50 * 0.60 + (calls - 150) * 0.50
else:
    bill = 200 + 50 * 0.60 + 50 * 0.50 + (calls - 200) * 0.40

print(bill)


