from flask import Flask, request, jsonify
import subprocess

app = Flask(__name)

def check_url_availability(url):
    try:
        # Run the "ping" command
        result = subprocess.run(["ping", "-c", "1", url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            return "URL is alive"
        else:
            return "URL is not alive"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/ping/<url>', methods=['GET'])
def ping(url):
    result = check_url_availability(url)
    return jsonify({'status': result})

if __name__ == '__main__':
    app.run(debug=True)