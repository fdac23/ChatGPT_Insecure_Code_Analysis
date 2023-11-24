from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

# Define a function to escape HTML characters
def escape_html(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

# Define a custom HTTP request handler
class CustomRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse the request for the username parameter
        parsed_url = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_url.query)
        username = query_params.get('username', [''])[0]

        # Construct the response with the "Hello [username]" message
        response_message = f"Hello {escape_html(username)}"

        # Send the response with a 200 OK status
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        # Write the response message to the client
        self.wfile.write(response_message.encode('utf-8'))

# Define the server address and port
server_address = ('', 8080)

# Create an HTTP server with the custom request handler
httpd = HTTPServer(server_address, CustomRequestHandler)

# Start the server
print("Server is running on port 8080...")
httpd.serve_forever()