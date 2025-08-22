selected_subjects = set()

while True:
    print("\n*================= Subject Management System =================*")
    print("1. Add Subject\n2. Remove Subject\n3. View Subjects\n4. Total Number of Unique Subjects\n5. Exit")

    choice = input("\nEnter your choice (1-5): ")
    
    if choice == '1':
        subject = input("Enter subject name to add: ")  
        if subject in selected_subjects:
            print(f"{subject} is already in the list!")
        else:
            selected_subjects.add(subject)
            print(f"{subject} has been added successfully.")
    
    elif choice == '2':
        if not selected_subjects:
            print("No subjects in the list!")
        else:
            subject = input("Enter subject name to remove: ")
            if subject in selected_subjects:
                selected_subjects.remove(subject)
                print(f"{subject} has been removed.")
            else:
                print(f"{subject} not found in the list.")
    
    elif choice == '3':
        if not selected_subjects:
            print("No subjects in the list!")
        else:
            print("\nList of Subjects:")
            for index, subject in enumerate(sorted(selected_subjects), 1):
                print(f"{index}. {subject}")
    
    elif choice == '4':
        print(f"\nTotal number of unique subjects: {len(selected_subjects)}")
    
    elif choice == '5':
        print("Thanks for Visiting.")
        break
    
    else:
        print("Invalid choice! Please try again.")
