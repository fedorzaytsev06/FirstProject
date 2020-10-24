def same_word(s1, s2):
    arr_str_1 = list(set(s1.split()))
    arr_str_2 = s2.split()
    for i in range(len(arr_str_1)):
        if arr_str_1[i] in arr_str_2:
            print(arr_str_1[i], "true")
        else:
            print(arr_str_1[i], "false")

    # dict=
    # for x in

same_word("cat cat dog", "cat pen")
