def solution(a):  # [0,1,0,1]-> 0 [0, 1, 1, 0]->2
    amount = 0
    for i in range(len(a) - 1):
        if a[i] == a[i + 1] and a[i] == 1:
            a[i + 1] = 0
            amount += 1
        elif a[i] == a[i + 1] and a[i] == 0:
            a[i + 1] = 1
            amount += 1
    return amount


print(solution([0, 1, 1, 0]))
