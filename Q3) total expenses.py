# Write a program to calculate the total expenses. Quantity
#  and price per item are input by the user and discount of 10% 
# is offered if the expense is more than 5000

qty = int(input("Enter the Quantity: "))
price = int(input("Enter the Price: "))

total = qty * price
print("Total price is", total)

if total > 5000:
    new = total - (total * 10 / 100)
    print("Discounted total is", new)
else:
    print("No discount applied")



        
        


        



