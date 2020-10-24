a = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
b = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
s = int(input())
result = ""
for i in range(len(a)):
    result += s // a[i] * b[i]
    s %= a[i]
print(result)
#"hello"*3 -> "hellohellohello"