# Write a program to determine whether the seller has made profit or incurred loss.
#  Also determine how much profit he made or loss he incurred. 
# Cost price and selling price of an item is input by the user


cost_price = float(input("Enter the Cost Price: "))
selling_price = float(input("Enter the Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"Profit of {profit}")

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print(f"Loss of {loss}")

else:
    print("No Profit, No Loss")

