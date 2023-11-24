from flask import Flask, request
import yaml

app = Flask(__name__)

def calculate_price(payload):
    try:
        # Load the YAML payload
        data = yaml.safe_load(payload)

        # Extract product_code and quantity
        product_code = data.get("product_code")
        quantity = data.get("quantity")

        if product_code is not None and quantity is not None:
            # Replace this with your price retrieval logic
            # For this example, we'll use dummy prices
            prices = {"product1": 10, "product2": 20, "product3": 30}

            if product_code in prices:
                price = prices[product_code] * quantity
                return str(price)
            else:
                return "Product not found"
        else:
            return "Missing product_code or quantity in the payload"

    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/calculate_price', methods=['GET'])
def get_price():
    yaml_payload = request.args.get('payload')
    if yaml_payload is not None:
        total_price = calculate_price(yaml_payload)
        return total_price
    return "Missing YAML payload as a query parameter."

if __name__ == '__main__':
    app.run(debug=True)
