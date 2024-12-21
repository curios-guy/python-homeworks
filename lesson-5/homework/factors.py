# initial value
integer = int(input("Please input positive integer: "))
factors = []

# finds factors of the given integer
def factorOut(num):
    for i in range(num+1):
        if i !=0 and num%i == 0 :
            factors.append(i)
            print(f"{i} is a factor of {num}")
    # return 


# checks if number is prime or composite
def isComposite():
    if len(factors) == 2:
        print(f"{integer} is prime number")
    else: print(f"{integer} is composite number")


# result
print(f"{factorOut(integer)}")
print(f"{isComposite()}")
# print(factors)
# print(range(integer))