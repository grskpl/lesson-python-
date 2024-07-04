def say_hi(name, age):
    if age > 0:
        return f"Hi. My name is {name} and I'm {age} years old"
    else:
        raise ValueError("Age should be a positive integer")


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'

try:
    say_hi("Alice", -25)
except ValueError as e:
    assert str(e) == "Age should be a positive integer"
else:
    raise AssertionError("Expected ValueError for negative age")

print('ОК')
