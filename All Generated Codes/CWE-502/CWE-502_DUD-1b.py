from flask import Flask, request, jsonify

app = Flask(__name)

@app.route('/get_name', methods=['POST'])
def get_name():
    data = request.get_json()

    if 'name' in data:
        name = data['name']
        return jsonify({'message': f'Name found: {name}'})

    return jsonify({'message': 'Name field not found'})

if __name__ == '__main__':
    app.run(debug=True)