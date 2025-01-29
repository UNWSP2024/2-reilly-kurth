#Author: Reilly Kurth 
#Date Written: 01/29/2025

item1 = float(input("Enter price of item 1: $"))
item2 = float(input("Enter price of item 2: $"))
item3 = float(input("Enter price of item 3: $"))
item4 = float(input("Enter price of item 4: $"))
item5 = float(input("Enter price of item 5: $"))

subtotal = (item1 + item2 + item3 + item4 + item5)
print("The subtotal of the purchases is ", subtotal)

tax = 0.07
sales_tax = subtotal * tax
print("The sales tax of the purchases is ", sales_tax)
