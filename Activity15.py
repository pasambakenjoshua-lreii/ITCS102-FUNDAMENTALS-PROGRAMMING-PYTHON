end = 0

for w in range(1,11):
    num = eval(input("Input a number"))
    if num % 2 == 1:
        end += num
print(f"The summation of all number is {end}")
