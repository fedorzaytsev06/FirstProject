x = int(input())
p = int(input())
y = int(input())
a = 0
while x < y:
    x *= (1 + p/100)
    print(x)
    x = int(x*100)/100
    print(x)
    a += 1
print(a)
