def find_max(list1):
    max_value = list1[0]
    for i in list1:
        if i > max_value:
            max_value = i
    return max_value
