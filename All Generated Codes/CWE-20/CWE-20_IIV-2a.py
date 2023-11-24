from urllib.parse import urlparse

def redirect_url(url):
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Get the domain name from the parsed URL
    domain = parsed_url.netloc
    
    if domain == "example.com":
        # Redirect the URL
        print(f"Redirecting to {url}")
        # You can add your redirection logic here
    else:
        # Return a 404 error
        print("404 Error: Page not found")

# Example usage:
url_to_redirect = "http://example.com/somepage"
url_to_not_redirect = "http://otherdomain.com/page"

redirect_url(url_to_redirect)
redirect_url(url_to_not_redirect)
