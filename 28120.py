def get_dividers(number):
    l = []
    # x = [1, 2, 3..number]
    for i in range(1, number + 1):
        if number % i == 0:
            l.append(i)
    return l


a = 10
b = 100
for i in range(a, b):
    d = get_dividers(i)
    if len(d) == 4:
        print(i, d)
# print(get_dividers(45))
