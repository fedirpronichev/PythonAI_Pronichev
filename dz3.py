import random


class Encryptor:
    def __init__(self, *numbers):
        self._numbers = numbers
        self._result = self._encrypt()

    def _encrypt(self):
        operations = {
            "add": sum(self._numbers),
            "subtract": self._numbers[0] - sum(self._numbers[1:]),
            "multiply": self._prod(),
            "divide": self._safe_divide()
        }
        return operations[random.choice(list(operations.keys()))]

    def _prod(self):
        result = 1
        for num in self._numbers:
            result *= num
        return result

    def _safe_divide(self):
        if len(self._numbers) > 1 and all(num != 0 for num in self._numbers[1:]):
            result = self._numbers[0]
            for num in self._numbers[1:]:
                result /= num
            return result
        return "Invalid operation"

    def __str__(self):
        return f"Encrypted result: {self._result}"


encryptor = Encryptor(10, 5, 2)
print(encryptor)
