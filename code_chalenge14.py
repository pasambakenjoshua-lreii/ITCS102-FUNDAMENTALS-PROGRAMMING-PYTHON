#Odd number compiler
#while Loop

name = input("Please put your name: \t") 
print("+++++++++++++++++++++++++++++")
print("Odd number compiler, type '0' to terminate the loop")

sum = 0
odd = ""
tuloy = True

while tuloy == True:
    num = eval(input("Please input a number --> "))
 
    if num % 2== 1:
        print("Odd number detected")
        odd += str(num) + ","
        sum += num
        continue
    elif num == 0:
        print("loop terminated")
        break
    else:
        if num % 2 == 0:
            print("Even number, skipping ... ")
        else:
            print("Invalid Number")
            continue

print(f"Hi {name}, The sum of all od number is {sum} ")
print(f"All the odd numbers you input is {odd}")