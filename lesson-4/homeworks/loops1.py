
# lists here
list1 = [1, 1, 2]
list2 = [2, 3, 4]

# open new variable
uncommons = []

# loop through list1
for element in list1:
    if element not in list2:
        uncommons.append(element)

# loop through list2
for element in list2:
    if element not in list1:
        uncommons.append(element)

# print result
print(uncommons)

