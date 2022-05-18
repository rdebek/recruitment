import json
import unittest

import requests

API_URL = 'http://127.0.0.1:5000'


class CustomerReportTests(unittest.TestCase):

    def test_adding_and_retrieving_report(self):
        sample_data = {
            'pay_by_link': [
                {
                    'created_at': '2021-05-13T01:01:43-08:00',
                    'currency': 'EUR',
                    'amount': 3000,
                    'description': 'Gym membership',
                    'bank': 'mbank',
                }
            ],
            'dp': [
                {
                    'created_at': '2021-05-14T08:27:09Z',
                    'currency': 'USD',
                    'amount': 599,
                    'description': 'FastFood',
                    'iban': 'DE91100000000123456789',
                }
            ],
            'card': [
                {
                    'created_at': '2021-05-13T09:00:05+02:00',
                    'currency': 'PLN',
                    'amount': 2450,
                    'description': 'REF123457',
                    'cardholder_name': 'John',
                    'cardholder_surname': 'Doe',
                    'card_number': '2222222222222222',
                },
                {
                    'created_at': '2021-05-14T18:32:26Z',
                    'currency': 'GBP',
                    'amount': 1000,
                    'description': 'REF123456',
                    'cardholder_name': 'John',
                    'cardholder_surname': 'Doe',
                    'card_number': '1111111111111111',
                },
            ]
        }
        sample_customer_id = 25

        #  adding report to database
        requests.post(f'{API_URL}/customer-report', json={**sample_data, 'customer_id': sample_customer_id})

        #  getting report from /report endpoint to compare results
        request = requests.post(f'{API_URL}/report', json=sample_data)
        report = json.dumps(request.json())

        #  getting last report from database
        last_report = requests.get(f'{API_URL}/customer-report/{sample_customer_id}').json()

        self.assertEqual(report, last_report)
