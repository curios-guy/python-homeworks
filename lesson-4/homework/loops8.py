#  Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

# A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

# numbers between 1 and 100
print("Prime numbers between 1 and 100:")

for num in range(2, 101):  
    isPrime = True  
    for divisor in range(2, int(num ** 0.5) + 1):  
        # if divisible it's not a prime number
        if num % divisor == 0:  
            isPrime = False
            break
    if isPrime:
        print(num, end=" ")
