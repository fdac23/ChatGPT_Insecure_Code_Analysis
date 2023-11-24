import re

# Define the regular expression pattern
redirect_pattern = re.compile(r'^/blog/post/(\d+)/$')

# Sample target URL
target_url = "/blog/post/123/"

# Use the regular expression to match the target URL
match = redirect_pattern.match(target_url)

# Check if the target URL matches the pattern
if match:
    # Extract the post ID from the match
    post_id = match.group(1)

    # Construct the redirect URL using the post ID
    redirect_url = f"/newpath/{post_id}/"
else:
    # Use a default URL if the target URL does not match
    redirect_url = "/default/"

# Redirect to the appropriate URL
print("Redirecting to:", redirect_url)
