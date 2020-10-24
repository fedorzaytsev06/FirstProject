def count_number(number, lst):
    k = 0
    for i in range(len(lst)):
        if number == lst[i]:
            k += 1
    return k


l = [1, 2, 2, 3]  # [1, 3]
r = []
for i in range(len(l)):
    elem = l[i]
    d = count_number(elem, l)
    if d == 1:
        print(elem)