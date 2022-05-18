import unittest

import requests

API_URL = 'http://127.0.0.1:5000'


class ReportTests(unittest.TestCase):
    def test_example_data(self):
        example_data = {
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
        expected_response = [
            {
                'date': '2021-05-13T07:00:05Z',
                'type': 'card',
                'payment_mean': 'John Doe 2222********2222',
                'description': 'REF123457',
                'currency': 'PLN',
                'amount': 2450,
                'amount_in_pln': 2450,
            },
            {
                'date': '2021-05-13T09:01:43Z',
                'type': 'pay_by_link',
                'payment_mean': 'mbank',
                'description': 'Gym membership',
                'currency': 'EUR',
                'amount': 3000,
                'amount_in_pln': 13494,
            },
            {
                'date': '2021-05-14T08:27:09Z',
                'type': 'dp',
                'payment_mean': 'DE91100000000123456789',
                'description': 'FastFood',
                'currency': 'USD',
                'amount': 599,
                'amount_in_pln': 2219,
            },
            {
                'date': '2021-05-14T18:32:26Z',
                'type': 'card',
                'payment_mean': 'John Doe 1111********1111',
                'description': 'REF123456',
                'currency': 'GBP',
                'amount': 1000,
                'amount_in_pln': 5208,
            }
        ]

        request = requests.post(f'{API_URL}/report', json=example_data)
        response = request.json()
        self.assertEqual(expected_response, response)

    def test_invalid_date(self):
        test_data = {'pay_by_link': [
            {
                'created_at': '123456',
                'currency': 'EUR',
                'amount': 1500,
                'description': 'placholder',
                'bank': 'ing',
            }
        ],
        }
        request = requests.post(f'{API_URL}/report', json=test_data)
        response_status = request.status_code
        self.assertEqual(400, response_status)
