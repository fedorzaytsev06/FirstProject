def power(n, a):
    amount = 1
    for i in range(a):
        amount = amount * n
    return amount

n = int(input("n="))
a = int(input("a="))
result = power(n, a)
print(result)
