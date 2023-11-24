from flask import Flask, request, jsonify
import yaml

app = Flask(__name)

@app.route('/', methods=['GET'])
def process_request():
    payload = request.args.get('payload')

    if not payload:
        return jsonify({'error': 'Payload parameter is missing'}), 400

    try:
        payload_data = yaml.safe_load(payload)
    except yaml.YAMLError:
        return jsonify({'error': 'Invalid YAML payload'}), 400

    if 'type' not in payload_data:
        return jsonify({'error': 'Type parameter is missing in payload'}), 400

    if payload_data['type'] == 'Create':
        return jsonify({'error': 'Create operation is not allowed'}), 400

    if payload_data['type'] == 'Update':
        if 'name' in payload_data and payload_data['name'] == 'UnsafeDeserialization':
            return jsonify({'error': 'UnsafeDeserialization is not allowed'}), 400

    return jsonify({'message': 'Request processed successfully'})

if __name__ == '__main__':
    app.run(port=5000)