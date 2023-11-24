# A sample environment dictionary with template mappings
env = {
    "templates": {
        "welcome_template": "Welcome, {{ name }}!",
    }
}

# Function to render a response from the environment
def render_response_from_env(environment, request_name):
    # Get the template from the environment
    templates = environment.get("templates", {})
    template = templates.get("welcome_template", "Hello, {{ name }}!")

    # Extract the 'name' parameter from the request (simulated here)
    name = request_name

    # Render the template with the 'name' parameter
    response = template.replace("{{ name }}", name)

    return response

# Function to handle the 'home' request
def home():
    # Simulated request name (you can obtain it from the actual request)
    request_name = "John"

    # Call the render_response_from_env function with the 'env' variable
    response = render_response_from_env(env, request_name)

    return response

# Example usage:
if __name__ == "__main__":
    response = home()
    print(response)