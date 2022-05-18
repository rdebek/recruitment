import sqlite3
from json import dumps

from flask import request, Response
from flask_restful import Resource

from src.endpoints.report import Report


class CustomerReport(Resource):
    def __init__(self):
        self.connection = sqlite3.connect('customer.db')

    def post(self):
        cur = self.connection.cursor()
        json = request.json
        if 'customer_id' in json:
            report = Report.generate_report(json)
            cur.execute(f"INSERT INTO customers VALUES ({json['customer_id']}, '{dumps(report)}')")
            self.connection.commit()
            self.connection.close()
            return Response(status=200)
        return Response(status=400)

    def get(self, customer_id: int):
        cur = self.connection.cursor()
        cur.execute(f'SELECT data FROM customers WHERE customer_id = {customer_id}')
        last_report = cur.fetchall()[-1][0]
        return last_report
