# initial values
number = int(input("Please input positive number: "))
factors = []

# gets factors of given number
def factorOut(num):
    for i in range(num+1):
        if i!=0 and num%i==0:
            factors.append(i)

# checks if given number is prime or not
def isPrime(num):
    factorOut(num)
    if len(factors) ==2:
        print(f"{number} is prime")
    else: print(f"{number} is composite")

isPrime(number)
# print(factors)