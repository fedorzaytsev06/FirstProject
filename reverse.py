def reverse(x):
    s = ""
    while x != 0:
        n = x % 10
        x //= 10
        s += str(n)
    return s


N = int(input())
print(reverse(N))
