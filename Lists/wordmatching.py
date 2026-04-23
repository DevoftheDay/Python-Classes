def match_words(words):
    ctr = 0
    lst = []

    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("List of words with first and last characters that are the same are: \n", lst)
    return ctr

count = match_words(['abc', 'cfc', 'xyz', 'yay', '34643'])
print("Number of words have the first and last character as the same are: \n", count)