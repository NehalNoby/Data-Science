shop=[]
n=int(input("Enter the number of items you want to add: "))
for i in range(n):
    item=input("Enter the item name: ")
    price=float(input("Enter the price of the item: "))
    quantity=int(input("Enter the quantity of the item: "))
    if price >50:
        discount=price *0.1
        price-=discount


    shop.append({"Item":item,"Price":price,"Quantity":quantity})
print(shop)