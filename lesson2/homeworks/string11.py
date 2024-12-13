text = input("Input text please: ")
numbers = "1 2 3 4 5 6 7 8 9 0"
new = numbers.split(" ")
print(numbers.split(" "))
if new not in text.lower():
    print("There is no digits in text")
else: print("There are digits in text.")