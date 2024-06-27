def calculator():
    while True:
        expression = input("Введіть вираз для обчислення: ")

        try:
            result = eval(expression)
            print("Результат:", result)
        except Exception as e:
            print("Помилка обчислення:", e)

        choice = input("Хочете продовжити роботу калькулятора? (y/n): ").lower()
        if choice != 'y' and choice != 'yes':
            print("До побачення!")
            break


calculator()
