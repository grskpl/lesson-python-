import keyword
import string
def is_valid_variable_name(name):
    if name[0].isdigit():
        return False

    if any(char.isupper() for char in name):
        return False

    allowed_characters = string.ascii_letters + string.digits + '_'
    if not all(char in allowed_characters for char in name):
        return False

    if name.count('_') == len(name) and len(name) > 1:
        return False

    if name in keyword.kwlist:
        return False

    return True



print(is_valid_variable_name("my_variable"))
print(is_valid_variable_name("variable_2"))
print(is_valid_variable_name("_variable"))
print(is_valid_variable_name("1variable"))
print(is_valid_variable_name("variableName"))
print(is_valid_variable_name("var!able"))
print(is_valid_variable_name("for"))
print(is_valid_variable_name("_"))
