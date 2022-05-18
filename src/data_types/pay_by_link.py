from src.data_types.payment import Payment


class PayByLink(Payment):
    def __init__(self, info_dict: dict) -> None:
        super().__init__(info_dict)
        self.bank = info_dict['bank']

    def get_payment_info(self) -> dict:
        payment_info = super().get_payment_info(type='pay_by_link', payment_mean=self.bank)
        return payment_info
