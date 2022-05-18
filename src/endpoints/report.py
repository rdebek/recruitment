from typing import List

from flask import request, Response
from flask_restful import Resource

from src.data_types.card import Card
from src.data_types.direct_payment import DirectPayment
from src.data_types.pay_by_link import PayByLink
from src.data_types.payment import InvalidDateFound


class Report(Resource):
    def post(self):
        json = request.json
        try:
            report = self.generate_report(json)
        except InvalidDateFound:
            return Response(status=400)
        return report

    @staticmethod
    def generate_report(json: dict) -> List[dict]:
        payments_array = []

        if 'pay_by_link' in json:
            for pay in json['pay_by_link']:
                payments_array.append(PayByLink(pay))

        if 'dp' in json:
            for pay in json['dp']:
                payments_array.append(DirectPayment(pay))

        if 'card' in json:
            for pay in json['card']:
                payments_array.append(Card(pay))

        payments_array.sort()

        return [pay.get_payment_info() for pay in payments_array]
