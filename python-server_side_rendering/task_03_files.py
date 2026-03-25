#!/usr/bin/python3

from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json_file():
    with open('products.json', 'r') as file:
        data = json.load(file)
    return data

def read_csv_file():
    with open('products.csv', 'r') as file:
        return list(csv.DictReader(file))

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:
        return render_template(
            'product_display.html',
            error="Wrong source",
            products=[]
        )

    if product_id:
        filtered_products = []

        for product in products_data:
            if str(product.get('id')) == str(product_id):
                filtered_products.append(product)

        if not filtered_products:
            return render_template(
                'product_display.html',
                error="Product not found",
                products=[]
            )

        return render_template(
            'product_display.html',
            products=filtered_products,
            error=None
        )

    return render_template(
        'product_display.html',
        products=products_data,
        error=None
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
