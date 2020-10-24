letters = {}
s = "sdfs dsfdsfs sdfds"
for elem in s:
    letters.setdefault(elem, 0)  # s : 0, s: 1, s: 2
    letters[elem] += 1
max_value = 0
max_letter = ""
for key, value in letters.items():
    print(key, value)
    if value>max_value:
        max_value = value
        max_letter = key
print(max_value, max_letter)
