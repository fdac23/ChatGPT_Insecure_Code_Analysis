from flask import Flask, request, redirect
import re

app = Flask(__name)

# Define the regular expression pattern
regex_pattern = r'.*example\.com.*'

@app.route('/redirect')
def redirect_route():
    target = request.args.get('target')

    # Check if the target matches the regular expression
    if re.match(regex_pattern, target):
        return redirect(target)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)