from src.data_types.payment import Payment


class Card(Payment):
    def __init__(self, info_dict: dict) -> None:
        super().__init__(info_dict)
        self.cardholder_name = info_dict['cardholder_name']
        self.cardholder_surname = info_dict['cardholder_surname']
        self.card_number = info_dict['card_number']

    def get_payment_info(self) -> dict:
        payment_info = super().get_payment_info(type='card', payment_mean=f'{self.cardholder_name}'
                                                                          f' {self.cardholder_surname}'
                                                                          f' {self.get_masked_card_number()}')
        return payment_info

    def get_masked_card_number(self) -> str:
        masked_card_number = self.card_number[:4] + 8 * '*' + self.card_number[-4:]
        return masked_card_number
