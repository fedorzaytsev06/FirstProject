def count(word):
    amount = 0
    for i in range(len(word)):
        if word[i] == "е":
            amount += 1
    return amount

s = input().split()
print(s)
for i in range(len(s)):
    word = s[i]
    if count(word) == 3:
        print(word)
