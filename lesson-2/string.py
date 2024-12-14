hello = """Hello
World 
SUP?"""

new = r"I\'m somet\bhing \t innit? \nnot joking"
print(hello)
print(new)
word = "I"


name = input("What's your name?")
age = int(input("What's your age?"))
print(f"Your name: {name} and {age} ")
print("YOur name: {name} and {age}" .format(name=name, age=age))
print("YOUR name: {} and {}" .format(name, age))
print(type(age))

print(f"Age - {age:>20}")
print(f"Name - {name:>20}")
print(f"{name:<12} - another name")
print(f"{age:<12} - another age")