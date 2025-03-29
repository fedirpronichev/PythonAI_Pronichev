# import random
# my_list = []
#
# for i in range(10):
#     my_list.append(random.randint(-10, 10))
#
# print(my_list)
# print("-" * 20)
#
# iterator = iter(my_list)
#
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
#
# interator = iter(my_list)
# for elem in interator:
#     print(elem)



# class Counter:
#     def __init__(self, max_number):
#         self.i = 0
#         self.max_number = max_number
#
#     def __iter__(self):
#         self.i = 0
#         return self
#
#     def __next__(self):
#         self.i += 1
#         if self.i > self.max_number:
#             raise StopIteration
#         return self.i
#
# cont = Counter(5)
#
# for elem in cont:
#     print(elem)
#
# print(30)
#
# cont = Counter(5)
#
#
# print(+38)
#
# cont = Counter(5)
#
# print(next(cont))
# print(next(cont))
#
# list_power_2 = [1 ** 2 for i in range(1,20,1) ]
# print(list_power_2)
#
# def raise_to_the_degrees(number, max_degrees):
#     for i in range(max_degrees + 1):
#         yield (number ** i)
#
# res = raise_to_the_degrees(2, 500)
# print(res)


class Helper:
    def __init__(self, work):
        self.work = work

    def __call__(self, work):
        return f"I will help you with your {self.work}. Afterwards I will help you with {work}."

helper = Helper("homework")
print(helper("cleaning"))ZeroDivisionError
