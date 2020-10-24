def RLE(s):
    amount = 1
    letter = ""
    result = ""  # AAB -> A2B
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            amount += 1
            letter = s[i - 1]
        else:
            if amount == 1:
                result += s[i - 1]
            else:
                result += letter + str(amount)
            amount = 1
    if amount == 1:
        result += s[-1]
    else:
        result += letter + str(amount)

    return result


new_s = RLE("ABBCC")
print(new_s)
print("abg"[-3])