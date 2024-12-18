# lists here
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# new variable
uncommons = []

for i in list1:
    if i not in list2:
        uncommons.append(i)

for i in list2:
    if i not in list1:
        uncommons.append(i)

print(f"Uncommon numbers in the list: {uncommons}")