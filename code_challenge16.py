

#student information system

import os 

print("Student Information System")
print("--------------------------")

student_records = {}

while True:
    print("Select from the options below \nA - Add Information\nB - Search a Record\nC - Delete a Record\nD - Modify a Record\nE - Exit")
    choice = input("Your Choice    ---> ").lower()

    if choice == 'a':
        os.system('cls')
        print("Adding Student Information")
        print("---------------------------")
        student_id = input("Key search for this student. use this pattern(course-INDO) -> ")
        first_name = input("Input student first name -> ").upper()
        last_name = input("Input student last name -> ").upper()
        course = input("Input student course -> ").upper()
        email = input("Input student email address -> ")

        #adding student to our dictionary
        student_records = {student_id : [first_name, last_name, course, email]}
        print("Data Saved")
        
        os.system('cls')
        continue
#Search
    elif choice == 'b':
        print("PRINTING STUDENT RECORD")

        for id, record in student_records.items():
                print(f"STUDENT ID {id} in STUDENT RECORD {record}")
        continue

#os.system('cls')
        
    elif choice == 'c':
        os.system('cls')
        print("SEARCH STUDENT RECORD")
        print("==========================")
        
        search_id = input("Input ID to search -- > ").lower()

        for id in student_records.keys():
            if search_id in student_records.keys():
                print("======================")
                print("\n\nRECORD FOUND")
                print("======================") 
            else:
                print("NO RECORD FOUND")

        continue
    elif choice == 'd':
        print("Editing Existing Record")
    elif choice == 'e':
        break
    else:
        ("Error")
