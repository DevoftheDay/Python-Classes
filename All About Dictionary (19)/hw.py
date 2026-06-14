test_dict = {'1': 72, '2': 63, '3': 72, '4': 72, '5': 59}

print("The original dictionary: " + str(test_dict))

K = 72


res = 0
for key in test_dict:
    if test_dict[key] == K:
        res += 1

print("The frequency of K is: " + str(res))