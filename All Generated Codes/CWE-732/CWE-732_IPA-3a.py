import os

# Define the content to write to the file
content = "U2FsdGVkX1/R+WzJcxgvX/Iw=="

# Write the content to the file
with open("secret.txt", "w") as file:
    file.write(content)

# Define the restrictive file permissions (e.g., read-only for the owner)
# You can adjust these permissions as needed
restrictive_permissions = 0o400  # Read-only for the owner

# Change the file permissions
os.chmod("secret.txt", restrictive_permissions)

print("File 'secret.txt' created and permissions changed to restrictive.")
