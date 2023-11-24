from flask import Flask, request
import subprocess

app = Flask(__name)

@app.route('/ping')
def ping():
    url = request.args.get('url')

    if url:
        try:
            # Run the 'ping' command and capture the output
            cmd = ['ping', '-c', '4', url]  # Ping 4 times
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()

            if process.returncode == 0:
                return stdout.decode('utf-8')
            else:
                return f"Error: {stderr.decode('utf-8')}"
        except Exception as e:
            return f"Error: {str(e)}"
    else:
        return "Please provide a URL as a query parameter."

if __name__ == '__main__':
    app.run(debug=True)
