#student information system

import os 

print("Student Information System")
print("--------------------------")

student_record = {}

while True:
    print("Select from the options below \nA - Add Information\nB - Search a Record\n - Delete a Record\nD - Modify a Record\nE - Exit")
    choice = input("Your Choice    ---> ").lower()
    if choice == 'a':
        print("Adding Student Information")
        print("-------------------")
        search_code = input("Key search for this student -> ")
        first_name = input("Input student first name -> ").upper()
        last_name = input("Input student last name -> ").upper()
        course = input("Input student course -> ")
        email = input("Input student email address -> ")
        student_records = {search_code : [first_name, last_name, course, email] }
        print("Data Saved")
        
        os.system('cls')
        continue
#Search
    elif choice == 'b':
        os.system('cls')
        code = input("input search code -> ")

        for w in student_records.keys():
            if code in student_records.keys():
                print("Record Found")

                for i in student_records.keys():
                    print(i)

            else:
                    print("No Reord Found")
#os.system('cls')
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        print("Editing Existing Record")
    elif choice == 'e':
        break
    else:
        ("Invalid Choice")
