s = input().split()
print(s)
for i in range(len(s)):
    word = s[i]
    if word[0] == word[-1]:
        print(word)