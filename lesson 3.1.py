def calculator():
    while True:
        try:
            num1 = float(input("Введіть перше число: "))
            num2 = float(input("Введіть друге число: "))
            operation = input("Введіть операцію (+, -, *, /): ")

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                print("Неправильна операція! Введіть одну з цих операцій: +, -, *, /")
                continue

            print(f"Результат: {num1} {operation} {num2} = {result}")

            choice = input("Бажаєте продовжити обчисленнями? (так/ні): ")
            if choice.lower() != 'так':
                break

        except ValueError:
            print("Помилка: введено неправильне число!")
        except ZeroDivisionError:
            print("Помилка: ділення на нуль!")


if __name__ == "__main__":
    calculator()
