def split_list(lst):
    n = len(lst)
    if n == 0:
        return [[], []]
    elif n % 2 == 0:
        mid = n // 2
    else:
        mid = n // 2 + 1

    first_list = lst[:mid]
    second_list = lst[mid:]

    return [first_list, second_list]





print(split_list([]))  # [[], []]


print(split_list([1, 2, 3, 4]))  # [[1, 2], [3, 4]]


print(split_list([1, 2, 3, 4, 5]))  # [[1, 2, 3], [4, 5]]
