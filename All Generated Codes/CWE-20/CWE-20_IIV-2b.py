from flask import Flask, redirect, request, jsonify

app = Flask(__name)

@app.route('/redirect/<path:url>')
def redirect_invalid_url(url):
    if 'example.com' in url:
        return redirect(url)
    else:
        return jsonify({'error': 'Invalid URL. URL must be from example.com.'}, 400)

if __name__ == '__main__':
    app.run(debug=True)