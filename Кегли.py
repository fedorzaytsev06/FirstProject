N = int(input("N="))
K = int(input("K="))
l = []
for i in range(N):
    l.append("I")
print(l)
for i in range(K):
    left = int(input("l="))
    right = int(input("r="))  # "I"->"."
    for i in range(left, right + 1):
        l[i - 1] = "."
    print(l)
