def get_divider_list(number):
    l = []
    for i in range(2, number):
        if number % i == 0:
            l.append(i)
    return l


l = 2
r = 10
for i in range(l, r + 1):
    x = get_divider_list(i)
    if len(x) == 2:
        print(x, i)
