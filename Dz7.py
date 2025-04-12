import requests  # імпортуємо бібліотеку для HTTP-запитів

class CurrencyConverter:

    def __init__(self):
        self.rates = {}

    def get_rates(self):
        response = requests.get("https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json")
        data = response.json()
        for item in data:
            self.rates[item['cc']] = item['rate']
        self.rates['UAH'] = 1.0  # додаємо гривню вручну

    def convert(self, amount, from_currency, to_currency):
        if from_currency != "USD":
            amount = amount / self.rates[from_currency]
        amount = round(amount * self.rates[to_currency], 2)
        return amount

converter = CurrencyConverter()
converter.get_rates()

while True:
    try:
        amount = float(input("Введіть суму валюти: "))
        from_currency = input("Введіть код валюти, яку ви вводите (наприклад, EUR, UAH, GBP): ")
        to_currency = "USD"

        converted_amount = converter.convert(amount, from_currency.upper(), to_currency)

        print("Сума у розмірі {} {} дорівнює {:.2f} USD".format(amount, from_currency.upper(), converted_amount))
        break

    except KeyError:
        print("Введено неправильний код валюти. Спробуйте ще раз.")

    except ValueError:
        print("Введено неправильну суму. Спробуйте ще раз.")
