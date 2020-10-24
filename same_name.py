def same_word(s):
    split = s.split()
    dict = {}
    for i in range(len(split)):
        if split[i] in dict.keys():
            print(split[i])
            break
        else:
            dict[split[i]] = i
same_word("asdasda sdsd gkg sdsd")