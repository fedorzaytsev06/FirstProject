def is_palindrome(number):  # int 567
    number = str(number)  # str "567"
    x = len(number) - 1  # index last elem
    for i in range(len(number) // 2):
        if number[i] != number[x]:
            return False
        x -= 1
    return True


def amount_palindromes(number):
    amount = 0
    for i in range(1, number):
        if is_palindrome(i):
            amount += 1
    return amount


K = int(input())
print(amount_palindromes(K))
