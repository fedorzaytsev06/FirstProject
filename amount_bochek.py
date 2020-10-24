n = int(input())
if n <= 10 or n >= 20:
    if (n % 10) == 0 or (5 <= (n % 10) <= 9):
        print(str(n) + " bochek")
    elif (n % 10) == 1:
        print(str(n) + " bochka")
    else:
        print(str(n) + " bochki")
else:
    print(str(n) + " bochek")