text = input("Input text please: ")
numberOfWords = text.split(" ")
newOne= ""
joinStr= newOne.join(numberOfWords)
print(joinStr)
# print(str(numberOfWords[0:]))
print(f"Your text: {text} \nNumber of words: {len(joinStr)}")