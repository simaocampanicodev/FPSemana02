phrase1 = input()
phrase2 = input()
words = ''
list_word1 = phrase1.split(' ')
list_word2 = phrase2.split(' ')
conj = set()
for i in list_word1:
    if i in list_word2:
        conj.add(i)
print(" ".join(list(conj)))