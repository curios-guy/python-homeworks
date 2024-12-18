txt = "hello"
output = ""

# vowels
vowels = "aeiou"

i = 0
while i < len(txt):
    output += txt[i]
    # writing a sign after every other 3 letters
    if (i + 1) % 3 == 0 or txt[i] in vowels:
        if i + 1 < len(txt):  
            output += "_"
    i += 1

print(output)