groceries=["Sugar","Rice","Wheat"]
# print(groceries)
# print(groceries[0])
# print(groceries[1])
# print(groceries[1:3])
# groceries.append("Milk")
# print(groceries)

# if "Sr" in groceries:
#     print("Sugar is founded in the list")
# else:
#     print("NO")    


# groceries.remove("Rice")

# a=input("Enter a item to be removed :  ")
# if a in groceries:
#     print(f"Removed {a} from the list",groceries.remove(a))
# else:
#     print("Item not found")    
# print(groceries)

for i,it in enumerate(groceries,start=1):
    print(i,it)


for i in groceries:
    print(i)