number_of_items=float(input("Please enter the amount of item(s)"))
while number_of_items<0:
    print("Invalid number of items")
    number_of_items=float(input("Please enter the amount of item(s)"))
shipping_cost_per_item=float(input("Please enter the shipping cost per item"))
while shipping_cost_per_item<0:
    print("Invalid cost")
    shipping_cost_per_item=float(input("Please enter the shipping cost per item"))
total=number_of_items*shipping_cost_per_item
if total>100:
    total*=9/10
print("The total cost is $",total)
