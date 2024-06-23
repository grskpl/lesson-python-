def move_zeros_to_end(nums):
    non_zero_index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero_index] = nums[i]
            non_zero_index += 1

    while non_zero_index < len(nums):
        nums[non_zero_index] = 0
        non_zero_index += 1

    return nums

nums = [0, 1, 0, 3, 12]
result = move_zeros_to_end(nums)
print(result)  # Виведе: [1, 3, 12, 0, 0]
