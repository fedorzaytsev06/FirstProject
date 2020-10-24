N = int(input())
s = ""
while N != 0:
    x = N % 2
    s += str(x)
    N //= 2# 1//2
#print(s[::-1])

for elem in reversed(s):
    print(elem)