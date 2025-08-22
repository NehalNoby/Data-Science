fruits={"Apple","Banana","Cherry","Date","Orange"}
a=input("Enter a fruit name: ")
if a in fruits:
    print(f"{a} is available in the set fruits.")
else:
    print(f"{a} is not found in the set fruits.")