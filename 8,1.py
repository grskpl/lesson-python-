def add_one(digits):
    num = int(''.join(map(str, digits)))

    num += 1

    result = list(map(int, str(num)))

    return result
