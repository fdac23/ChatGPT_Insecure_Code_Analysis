from flask import Flask, request, jsonify
import subprocess

app = Flask(__name)

def ping_decorator(url):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = subprocess.run(["ping", "-c", "4", url], stdout=subprocess.PIPE, text=True)
            return func(url, result.stdout)
        return wrapper
    return decorator

@app.route('/ping/<url>')
@ping_decorator("<url>")
def ping(url, output):
    return jsonify({"url": url, "ping_output": output})

if __name__ == '__main__':
    app.run(debug=True)