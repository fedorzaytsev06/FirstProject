def count_dividers(number):
    l = []
    amount = 0
    for i in range(2, number):
        if number % i == 0:
            amount += 1
            l.append(i)
    return l


l = 2
r = 20
for i in range(l, r):
    dividers = count_dividers(i)
    if len(dividers) == 3:
        print(dividers)
