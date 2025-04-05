def calculator_decorator(func):
    def wrapper(expression):
        try:
            result = func(expression)
            print(f'Результат: {result}')
            return result
        except ZeroDivisionError:
            print('Помилка: Ділення на нуль!')
        except SyntaxError:
            print('Помилка: Неправильний синтаксис виразу!')
        except NameError:
            print('Помилка: Невідомі символи у виразі!')
        except Exception as e:
            print(f'Інша помилка: {e}')
    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)

calculate("10 + 5")
calculate("10 / 0")
calculate("10 +")
calculate("abc + 1")