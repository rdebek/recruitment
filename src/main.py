from flask import Flask
from flask_restful import Api

from src.endpoints.customer_report import CustomerReport
from src.endpoints.report import Report

if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Report, '/report')
    api.add_resource(CustomerReport, '/customer-report', endpoint='/post')
    api.add_resource(CustomerReport, '/customer-report/<int:customer_id>', endpoint='/get')
    app.run(debug=True)
