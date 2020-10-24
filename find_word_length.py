def find_word(s):
    # "sadasd sadasd asdasd"
    split = s.split()
    min_word = split[0]
    for word in split:
        if len(word) < len(min_word):
            min_word = word
    return len(min_word)


print(find_word("dsfdsf dsfdsfdsfsdf dsfdsfsdsf dsfdfdsfsdfs nn"))
gaedfs