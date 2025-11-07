#creating functions
#keyword, def = define
#code REUSABILITY

def inject(name):
    print(f"Hello {name}, How are you? ")

inject("Garrick")
inject("Mctavish")
inject("Riley")


def summation(x):
    sum = 0
    for q in range(x, 0, -1):
        sum += q
    print(f" The sum of {x} is {sum}")
