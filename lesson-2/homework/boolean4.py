a= float(input("Input any number: "))
b= float(input("Input any number: "))
c= float(input("Input any number: "))

if a==b and b==c:
    print("Numbers are equal!")
elif a==b or b==c or a==c:
    print("2 of them are equal")
else: print("None of them are equal!")