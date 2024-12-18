# name = input("Name: ")
# print(f"Hello {name}")

#functions


def new(y):
    return y*y;

def square(x):
    return x*x*x
for i in range(5):
    print(f"Three times multplied version of {i} is {square(i)}")






houses={"Harry": "gryffindor", "Draco": "slytherin"}

houses["Hermione"] = "gryffindor"

print(houses["Hermione"])



# lists
names=["Harry", "Hermione", "Larry", "Greta"]
just_name="Alisher"
names.append("Alish")

names.sort()

print(names)

# loops
for i in names:
    print(i)

for char in just_name:
    print(char)

#sets
s=set();

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)

print(s)
print(f"The set has {len(s)} elements.")


#my work
var = input("Number: ")
print(type(var))
if type(var) == int:
    if var > 0:
        print("Number is positive")
    elif var < 0:
        print("Number is negative")
    else:
        print("Number is zero you dummy")
elif type(var) == str:
    print("You inputted str")
else:
    print("You stupid @$%#$")

