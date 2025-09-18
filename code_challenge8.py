print("Welcome to multiplication table maker:")
num = eval(input("Enter a number: "))

for n in range (1, 11):
   result = num*n
    print(F"{num}x{n} = {result}")
