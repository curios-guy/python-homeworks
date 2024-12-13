text = input("Input text: ")
words = text.split(" ")
joint = "".join(i[0].upper() for i in words)
print(joint)
