def swap_elements(numbers):
    i = 0
    while i < (len(numbers) - 1):
        numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
        i += 2
    print(numbers)


l = []
N = int(input())
for j in range(N):
    x = int(input())
    l.append(x)

swap_elements(l)
