N = int(input("n="))
#l = []
amount = 0
for i in range(N):
    x = int(input("x="))
    #l.append(x)
    if x == 0:
        amount += 1
if amount > 0:
    print("YES")
else:
    print("NO")
