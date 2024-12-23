# main decorator 
def check(func):
    def wrapper(a,b):
        try: 
            return print(func(a,b))
        except ZeroDivisionError:
            return print("Denominator can't be zero")
    return wrapper
   
# calling the function
@check
def div(a,b):
    return a/b

# output
num1 = int(input("Input number 1: "))
num2 = int(input("Input number 2: "))

div(num1, num2)