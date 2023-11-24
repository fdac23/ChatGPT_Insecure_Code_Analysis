from flask import Flask, request, jsonify
import yaml

app = Flask(__name)

# Define a function to retrieve the price for a product code (replace with your own logic)
def get_price_for_product_code(product_code):
    # Example price lookup logic
    price_data = {
        'productA': 10.0,
        'productB': 15.0,
        'productC': 20.0,
    }
    return price_data.get(product_code, 0.0)

@app.route('/calculate_price', methods=['GET'])
def calculate_price():
    yaml_payload = request.args.get('payload')

    if not yaml_payload:
        return jsonify({'error': 'YAML payload is missing'}), 400

    try:
        payload_data = yaml.safe_load(yaml_payload)

        if 'product_code' not in payload_data or 'quantity' not in payload_data:
            return jsonify({'error': 'Invalid YAML payload. Missing product_code or quantity'}), 400

        product_code = payload_data['product_code']
        quantity = payload_data['quantity']

        price = get_price_for_product_code(product_code)
        total_price = price * quantity

        result = {'total_price': total_price}
        return jsonify(result)

    except yaml.YAMLError:
        return jsonify({'error': 'Invalid YAML payload'}), 400

if __name__ == '__main__':
    app.run(debug=True)