# initial values
principalAmount = float(input("Please input the amount of money you want to invest: "))
percentage = float(input("By how much percentege you want it to increase each year: "))
years = int(input("Please input exact year of years (1/2/3...), not the float (1.2/3.1...): "))

print("---------------------------")

# calculates the investment till given years
def invest(amount, percent, year):
    for i in range(year):
        amount += amount * (percent / 100)
        print(f" Year {i+1}: your account has {round(amount, 2)}")

# prints result
print(f"{invest(principalAmount, percentage, years)}")

