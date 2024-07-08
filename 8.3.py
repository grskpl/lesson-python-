def find_unique_value(nums):
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in nums:
        if count_dict[num] == 1:
            return num

    return None

print(find_unique_value([1, 2, 3, 2, 1]))
print(find_unique_value([5, 5, 6, 6, 7, 7, 8]))
print(find_unique_value([3, 3, 4, 4, 5]))

