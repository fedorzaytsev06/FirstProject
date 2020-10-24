x = int(input())  #
y = int(input())
s = x
day = 1
while s < y:
    day += 1
    print("----")
    print(s)
    s = 1.1 * s
    print(s)
    print("-----")
print(day)
print(s)
