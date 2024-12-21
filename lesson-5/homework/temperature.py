# gets initial value
fInp = float(input("Please input fahrenheit: "))
# uses function
fahrenheit = lambda fahren : round((fahren - 32) * 5/9, 2)
# prints result using farenheit function
print(f"{fInp} fahrenheit is {fahrenheit(fInp)} celsius")


print("------------------------")

# gets initial value
cInp = float(input("Please input celsius: "))
# uses function
celsius = lambda cels : round(cels * 9/5 + 32, 2)
# prints result using celsius function
print(f"{cInp} celsius is {celsius(cInp)} fahrenheit")



# # gets initial values
# fahrenheit = float(input("Please input Fahrenheit degree: "))
# celsius = float(input("Please input Celcius degree: "))

# # fahrenheit to celcius function
# def convert_cel_to_far(fahren):
#     celcius =  round((fahren - 32) * 5/9, 2)
#     return celcius

# # celcius to fahrenheit function
# def convert_far_to_cel(cels):
#     fahrenheit =  round(cels * 9/5 + 32, 2)
#     return fahrenheit

# # if 

# print(f"{fahrenheit} fahrenheit equals to {convert_cel_to_far(fahrenheit)} celcius")
# print(f"{celsius} celsius equals to {convert_far_to_cel(celsius)} fahrenheit")

