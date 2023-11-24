from flask import Flask, request, render_template_string

app = Flask(__name)

# Mock environment with templates (you can replace this with your actual template loading logic)
env = {
    "template": "Hello, {{ name }}!"
}

def render_response_from_env(env, name):
    template = env.get("template", "")
    rendered_template = render_template_string(template, name=name)
    return rendered_template

@app.route('/home')
def home():
    name = request.args.get('name', 'World')
    response = render_response_from_env(env, name)
    return response

if __name__ == '__main__':
    app.run(debug=True)
