from src.data_types.payment import Payment


class DirectPayment(Payment):
    def __init__(self, info_dict: dict) -> None:
        super().__init__(info_dict)
        self.iban = info_dict['iban']

    def get_payment_info(self) -> dict:
        payment_info = super().get_payment_info(type='dp', payment_mean=self.iban)
        return payment_info
