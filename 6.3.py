def multiply_digits_until_single_digit(n):
    digits = list(str(n))

    while len(digits) > 1:
        product = 1
        for digit in digits:
            product *= int(digit)

        digits = list(str(product))

    if digits:
        return int(digits[0])
    else:
        return 0


num = int(input("Введіть ціле число: "))
result = multiply_digits_until_single_digit(num)
print(f"Результат перемноження цифр до отримання однієї цифри, яка менше або дорівнює 9: {result}")
