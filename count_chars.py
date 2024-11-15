phrase = input()
chars = {}
phrase = phrase.replace(" ", "")
for char in phrase:
    if char in chars:
        chars[char] += 1
    else:
        chars[char] = 1
print(chars)