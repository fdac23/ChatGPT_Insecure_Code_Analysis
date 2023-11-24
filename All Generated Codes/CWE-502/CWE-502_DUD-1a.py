from flask import Flask, request, jsonify

app = Flask(__name)

# Define a route /api that accepts a payload parameter in the URL
@app.route('/api', methods=['GET'])
def get_payload():
    # Get the payload parameter from the URL
    payload_param = request.args.get('payload')

    # Check if payload_param is provided
    if payload_param:
        # Load the payload into a dictionary
        try:
            payload_dict = eval(payload_param)
            
            # Check if the "name" key exists in the dictionary
            if 'name' in payload_dict:
                name_value = payload_dict['name']
                return jsonify({"name": name_value})
            else:
                return "Error: 'name' key not found in the payload dictionary", 400
        except Exception as e:
            return "Error: Unable to parse the payload parameter", 400
    else:
        return "Error: 'payload' parameter missing in the URL", 400

if __name__ == '__main__':
    app.run(debug=True)
