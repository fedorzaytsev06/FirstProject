def get_dividers(number):
    l = []
    for i in range(2, number + 1):
        if i % 2 == 0 and number % i == 0:
            l.append(i)
    return l

l = 2
r = 16
for i in range(l, r + 1):
    dividers = get_dividers(i)
    print(i, dividers)
    if len(dividers) == 4:
        print(dividers)
