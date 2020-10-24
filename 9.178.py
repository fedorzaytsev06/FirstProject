# s = input()
# s = list(s)
# print(s)
# for i in range(len(s)):
#     if s[i] == "a":
#         s[i] = "o"
# r = "".join(s)
# print(r)
# for i in range(len(s)):
#     if s[i-1] = a:
#         s[i] = "o"
s = "aabbccdd"  # abcd

# s = list(s)
# result_str = ""
# for i in range(len(s)):
#     if s[i] not in result_str:
#         result_str += s[i]
# print(result_str)

s = input().split()
print(s)

max_word = s[0]

for i in range(len(s)):
    current_word = s[i]
    if len(current_word) > len(max_word):
        max_word = current_word
print(max_word)
# abc  l = n//2
# abcd index=n//2, n//2-1
remove_indexes = []
remove_indexes.append(len(max_word) // 2)
if len(max_word) % 2 == 0:
    remove_indexes.append(len(max_word) // 2 - 1)
print(remove_indexes)

r = ""
for i in range(len(max_word)):
    if i not in remove_indexes:
        r += max_word[i]
print(r)
