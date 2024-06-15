def shift_last_to_first(lst):
    if len(lst) <= 1:
        return lst

    last_element = lst.pop()
    lst.insert(0, last_element)

    return lst



print(shift_last_to_first([]))  # []


print(shift_last_to_first([1]))  # [1]


print(shift_last_to_first([1, 2, 3, 4, 5]))  # [5, 1, 2, 3, 4]


print(shift_last_to_first(['a', 'b', 'c', 'd']))  # ['d', 'a', 'b', 'c']
