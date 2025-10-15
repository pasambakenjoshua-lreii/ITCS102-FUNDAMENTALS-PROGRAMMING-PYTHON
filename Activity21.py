#washing machine cleaning
#(pass) dummy code

smelly = True
while smelly == True:
    confirm = input("Do you want to continue washing the clothes? (yes, no)").lower()

    if confirm == 'yes':
        print("continue the cycling")
        continue
    elif confirm == 'no' :
        print("cycling stop")
        break
    else:
        print("Invalid Input")
        continue
