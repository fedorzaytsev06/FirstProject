def is_simple(number):
    l = []
    for i in range(2, number):
        if number % i == 0:
            l.append(i)

    if len(l) > 0:
        return False
    else:
        return True


l = 2
r = 10
ls = []
for i in range(l, r):
    ls.append(i)
print(ls)

for i in range(len(ls)):
    if is_simple(ls[i]):
        print((i+1), ls[i])
