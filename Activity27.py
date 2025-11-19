print("Adding Data to Dictionary ->")
print(" ========================== ")
proceed = True

empty_dictionary = {}

def print_anime():
    for anime in empty_dictionary.values():
        print (f"Anime name -- {anime}")
    
while proceed == True:
    keys = input("Input anime Name ->")
    values = input("Enter   -> ")

    empty_dictionary [keys] = values

    choice = input("Would you like to continue adding anime (y/n)").lower ()

    if choice == 'y' :
        print("Continuing ... ")
        continue
    elif choice == 'n' :
        print("program stops")
        break
    else:
        print("Invalid Input")
        continue
