def which_are_in():
    list1 = list(input().split(", "))
    list2 = list(input().split(", "))
    new_list = []
    for word in list1:
        for word2 in list2:
            if word in word2:
                new_list.append(word)
                break
    return new_list


print(which_are_in())
