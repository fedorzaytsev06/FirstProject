def numder_ofzeroes(N):
    x = 0
    while N != 0:
        last_number = N % 10
        if last_number == 0:
            x += 1
        N //= 10
    return x


N = int(input())
print(numder_ofzeroes(N))
