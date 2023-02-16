import requests, json
from config import values

class ConvercionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(base: str, quote: str, amount: str):

        if base == quote:
            raise ConvercionException(f'Не удалось перевести одинаковые валюты: {base}-{quote} \n /help')

        try:
            base_ticker = values[base]
        except KeyError:
            raise ConvercionException(f'Не удалось обработать валюту {base} \n /help')

        try:
            quote_ticker = values[quote]
        except KeyError:
            raise ConvercionException(f'Не удалось обработать валюту {quote} \n /help')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvercionException(f'Не удалось обработать количество {amount} \n /help')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        result = json.loads(r.content)[values[quote]]
        result = round((result * amount), 2)

        return result