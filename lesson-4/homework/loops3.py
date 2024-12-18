# lists here
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

# variable here
uncommons=[]

# loop the list1
for e in list1:
    if e not in list2:
        uncommons.append(e)

# loop the list2
for e in list2:
    if e not in list1:
        uncommons.append(e)

print(f"Uncommons are: {uncommons}")