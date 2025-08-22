shopping_cart = []
while True:
    print("Menu:\n1. Add Item\n2. Remove Item\n3. View Cart\n4. Number of items in cart\n5. Exit")
    choice = input("Enter your choice (1-5): ")
    
    if choice == "1":
        item = input("Enter the item to add: ")   
        shopping_cart.append(item)
        print(f"Added {item} to the shopping cart.")
    
    elif choice == "2":
        item = input("Enter the item to remove: ")
        if item in shopping_cart:   
            shopping_cart.remove(item)
            print(f"Removed {item} from the shopping cart.")
        else:
            print(f"{item} not found in the shopping cart.")
    
    elif choice == "3":
        if shopping_cart:
            print("Shopping Cart Items:")
            for item in shopping_cart:
                print(item)
        else:
            print("Your shopping cart is empty.")
    
    elif choice == "4":
        print(f"Number of items in cart: {len(shopping_cart)}")

    elif choice == "5":
        print("Thank you for using the shopping cart!")
        break
    
    else:
        print("Invalid choice! Please try again.")