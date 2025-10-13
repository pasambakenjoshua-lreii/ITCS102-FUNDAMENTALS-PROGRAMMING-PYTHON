print("\t\t", end="*")
for x in range(1,12,1):
    for y in range(12,x,-1):
        print(" ", end=' ')
    for z in range(1,x,1):
        print("*", end=" ")
    for t in range(1,x,1):
        print("*", end=" ")
    print()
for x in range(1,12,1):
    for y in range(1,x,1):
        print(" ", end=' ')
    for z in range(12,x,-1):
        print("*", end=" ")
    for t in range(12,x,-1):
        print("*", end=" ")
    print()
print("\t\t" "*")
