import os

# Create and write to the file
with open('secret.txt', 'w') as file:
    file.write('U2FsdGVkX1/R+WzJcxgvX/Iw==')

# Change the file permissions to 128 (in octal format)
os.chmod('secret.txt', 0o200)

# Get and print the file permissions in octal format
file_permissions = oct(os.stat('secret.txt').st_mode & 0o777)
print(f'File permissions: {file_permissions}')