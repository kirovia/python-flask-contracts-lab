#!/usr/bin/env python3

from flask import Flask, request, current_app, g, make_response

contracts = [{"id": 1, "contract_information": "This contract is for John and building a shed"},{"id": 2, "contract_information": "This contract is for a deck for a buisiness"},{"id": 3, "contract_information": "This contract is to confirm ownership of this car"}]
customers = ["bob","bill","john","sarah"]
app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/contract/<int:id>')
def contract_find(id):
    contract = [c for c in contracts if c["id"] == int(id)]
    if len(contract) == 0:
        return "no contract found", 404
    return contract[0]["contract_information"], 200
    
@app.route('/customer/<customer_name>')
def customer(customer_name):
    if customer_name in customers:
        return customer_name, 204
    return "no customer found", 404