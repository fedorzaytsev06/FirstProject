s = input().split()
print(s)
r=0
for i in range(len(s)):
    word = s[i]
    if word[-1] == "р":
        r+=1
print(r)