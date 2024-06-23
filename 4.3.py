import random

n = random.randint(3, 10)

random_list = [random.randint(1, 100) for _ in range(n)]
print("Початковий список:", random_list)

if len(random_list) >= 3:
    new_list = [random_list[0], random_list[2], random_list[-2]]
    print("Новий список:", new_list)
else:
    print("Початковий список має менше ніж 3 елементів, неможливо створити новий список.")
