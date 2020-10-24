s = input().split() # [sdfsdf, sdfs, dsfs]
print(s)
r=0
for i in range(len(s)):
    # if s[0] == "н":
    word = s[i]
    if word[0] == "n":
        r+=1
print(r)

