def f(strs):
    words_dict = {}
    for word in strs:
        #letter_set = set(word)
        key = ''.join(sorted(word))

        if key in words_dict:
            words_dict[key].append(word)
        else:
            words_dict[key] = [word]

    result = [value for value in words_dict.values()]
    return result


