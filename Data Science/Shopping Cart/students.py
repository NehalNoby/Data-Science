students_records = {}
while True:
    print ("*----------STUDENT RECORDS MENU----------*")
    print("Enter your choice:\n1.Add Student\n2.Update Student\n3.Remove Student\n4.View all Students\n5.Search Student\n6.Total Number of Students\n7.Exit")
    choice= input("Enter your choice (1-7): ")      
    if choice =="1":
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        students_records[roll] = name
        print(f"New Student added: {roll} - {name}")

    elif choice =="2":
        roll_no=input("Enter the Roll Number to Update: ")
        if roll_no in students_records:
            new_name=input("Enter the name of the student:")
            students_records[roll_no] = new_name
            print(f"Student of Roll Number{roll_no} updated successfully.")
        else:
            print("Student Not Found!!!")

    elif choice =="3":
        roll_no=input("Enter the Student Roll Number to Remove:")
        if roll_no in students_records:
            remove=students_records.pop(roll_no)
            print(f" Student Removed Successfully: {roll_no} - {remove}")
        else:
            print("Student Not Found!!!")

    elif choice =="4":
        print("List of all students:\n")
        for roll,name in students_records.items():
            print(f"Roll No: {roll} | Name: {name}")
    elif choice =="5":
        roll_no=input("Enter the Roll Number to Search:")
        if roll_no in students_records:
            print(f"Student Found Successfully: Roll No: {roll_no} | Name: {students_records[roll_no]}")
        else:
            print("Student Not Found!!!")
    elif choice =="6":
        print(f"Total Number of Students: {len(students_records)}\n\n\n\n\n\n\n\n\n\n\n\n\n")

    elif choice==7:
        print("Exiting program!!!!!!!!!!!!!")
        break
    else:
        print("Invalid choice! Please try again.")

        
