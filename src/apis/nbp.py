from math import floor

import requests

NBP_API_BASE_STRING = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/{}/?format=json'


class Nbp:
    @staticmethod
    def get_amount_in_pln(amount: int, currency: str, date: str) -> int:
        """
        Function that converts USD, GBP, EUR to PLN

        Args:
            amount: The amount in one of currencies mentioned above.
            currency: Currency name.
            date: Date in ISO format.

        Returns:
            Amount converted to PLN rounded down to grosz.
        """
        if currency == 'PLN':
            return amount
        request = requests.get(NBP_API_BASE_STRING.format(currency, date[:date.find('T')]))
        return floor(request.json()['rates'][0]['bid'] * amount)
