# print(18 / 8)
# print("програма продовжує працювати")

# try:
#     print(10 / 6)
#     print("програма продовжує працювати")
# except ZeroDivisionError:
#     print("Неможливо ділити на 0")
# except ArithmeticError:
#     print("Виникла арифметична помилка")
#
# print("програма продовжує працювати")




# class BuildingError(Exception):
#     def __str__(self):
#         return "З такою кількістю матеріалів неможливо побудувати будинок"
#
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Достатньо матеріалів"
#     else:
#         raise BuildingError(amount_of_material)
#
#
#
# material = 123
# check_material(material, 300)

# try:
#     numerator = int(input("Введіть чисельник: "))
#     denominator = int(input("Введіть знаменник: "))  # Додано знак "="
#     print(numerator / denominator)
# except ZeroDivisionError:
#     print("Помилка: Ділення на 0 неможливе")
# except ValueError:
#     print("Помилка: Введенні данні не є числом")


import warnings

warnings.simplefilter("ignore", SyntaxWarning)
warnings.simplefilter("always", ImportWarning)
warnings.warn("Warning, no code here", SyntaxWarning)

try:
    warnings.warn("Warning, module not imported", ImportWarning)
    raise Exception("Forced exception")  # Raising an exception to trigger except
except Exception:
    print("Warning")
