def is_palindrome(text):
    alphanumeric_text = ''.join(char.lower() for char in text if char.isalnum())

    return alphanumeric_text == alphanumeric_text[::-1]

assert is_palindrome('A man, a plan, a canal: Panama') == True
assert is_palindrome('0P') == False
assert is_palindrome('a.') == True
assert is_palindrome('aurora') == False
print("ОК")
