from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

# Define a sample environment
env = {
    "template": "Hello, {{ name }}!",
}

# Render a response from the environment
def render_response_from_env(env):
    name = request.args.get("name", "Guest")
    template = env.get("template", "Hello, {{ name }}!")

    rendered_template = render_template_string(template, name=name)
    return jsonify({"message": rendered_template})

# Home function that calls render_response_from_env
@app.route('/')
def home():
    response = render_response_from_env(env)
    return response

if __name__ == '__main__':
    app.run(debug=True)