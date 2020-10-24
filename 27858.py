def get_dividers(number):
    l = []
    for i in range(1, number + 1):
        if number % i == 0:
            l.append(i)
    return l


l = 80
r = 90
mx_div = 0
mx_val = l
for i in range(l, r + 1):
    dividers = get_dividers(i)
    if len(dividers) >= mx_div:
        mx_div = len(dividers)
        mx_val = i

print(mx_div, mx_val)
