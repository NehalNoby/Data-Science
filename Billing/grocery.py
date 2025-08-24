items=["Milk","Bread","Egg"] 
price=[40,25,5]
total_amount=0
items_bought=int(input("How many items you buy? "))
for i in range(items_bought):
    item=input("Enter the item name: ")
    quantity=int(input("Enter the quantity: "))
    if item in items:
        index=items.index(item)
        amount=price[items.index(item)]*quantity
        print(f"Price of {quantity} {item} is {amount}")  
    else:
        print(f"{item} is not available")
    total_amount+=amount
    if total_amount>500:
        discount=total_amount*0.1
        total_amount-=discount
    elif total_amount>1000:
        discount=total_amount*0.2
        total_amount-=discount
print(f"Total amount to be paid is {total_amount}")