from flask import Flask, request, jsonify

app = Flask(__name__)

# Define a dictionary to store product prices based on product codes
product_prices = {
    "productA": 10.00,
    "productB": 20.00,
    "productC": 30.00,
}

def calculate_total_price(product_code, quantity):
    if product_code in product_prices:
        price_per_unit = product_prices[product_code]
        total_price = price_per_unit * quantity
        return total_price
    else:
        return None

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    product_code = request.args.get('product_code')
    quantity = int(request.args.get('quantity'))

    total_price = calculate_total_price(product_code, quantity)

    if total_price is not None:
        return jsonify({'total_price': total_price})
    else:
        return jsonify({'error': 'Invalid product code'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)