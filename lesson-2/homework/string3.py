text = str(input("Enter some text: "))
upper = text.upper()
lower = text.lower()

if text.strip():
    print(f"You entered: {text} \nUppercase: {upper} \nLowercase {lower}")
else:
    print("Please enter something")
