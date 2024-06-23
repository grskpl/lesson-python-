def sum_even_index_elements_multiply_last(arr):
    if not arr:
        return 0

    sum_even_index = 0

    for i in range(0, len(arr), 2):
        sum_even_index += arr[i]

    last_element = arr[-1]

    return sum_even_index * last_element


print(sum_even_index_elements_multiply_last([1, 2, 3, 4, 5]))
print(sum_even_index_elements_multiply_last([2, 4, 6, 8]))
print(sum_even_index_elements_multiply_last([]))
