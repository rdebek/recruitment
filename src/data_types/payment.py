from dateutil import parser
from dateutil.tz import UTC

from src.apis.nbp import Nbp


class Payment:

    def __init__(self, info_dict: dict) -> None:
        self.created_at = info_dict['created_at']
        self.currency = info_dict['currency']
        self.amount = info_dict['amount']
        self.description = info_dict['description']

    def __lt__(self, other):
        try:
            return parser.isoparse(self.created_at) < parser.isoparse(other.created_at)
        except ValueError:
            raise InvalidDateFound from ValueError

    def get_payment_info(self, **kwargs) -> dict:
        return {**kwargs, **{'date': self.get_utc_date(), 'description': self.description,
                             'amount': self.amount,
                             'currency': self.currency,
                             'amount_in_pln': Nbp.get_amount_in_pln(self.amount, self.currency, self.created_at)}}

    def get_utc_date(self) -> str:
        try:
            date = parser.isoparse(self.created_at)
        except ValueError:
            raise InvalidDateFound from ValueError
        date_utc = date.astimezone(UTC)
        return date_utc.strftime('%Y-%m-%dT%H:%M:%SZ')


class InvalidDateFound(Exception):
    pass
