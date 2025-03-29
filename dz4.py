import random


def divider(a, b):
    try:
        if a < b:
            raise ValueError("a is less than b")
        if b > 100:
            raise IndexError("b is greater than 100")
        return a / b
    except Exception as e:
        print(f"Error: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, (): 15, 8: 4}
result = []

for key in data:
    try:
        res = divider(key, data[key])
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"Unexpected error: {e}")

print(result)
