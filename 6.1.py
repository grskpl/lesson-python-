import string


def characters_between(input_str):
    start_char, end_char = input_str.split('-')

    start_index = string.ascii_letters.index(start_char)
    end_index = string.ascii_letters.index(end_char)

    result = string.ascii_letters[start_index:end_index + 1]

    return result


print(characters_between("a-c"))  # виведе: abc
print(characters_between("a-a"))  # виведе: a
print(characters_between("s-H"))  # виведе: stuvwxyzABCDEFGH
print(characters_between("a-A"))  # виведе: abcdefghijklmnopqrstuvwxyzA
