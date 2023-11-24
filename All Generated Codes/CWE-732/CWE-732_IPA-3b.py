import os

# Super secret information
super_secret_info = "This is super secret info."

# Create a file and write the super secret info to it
file_name = "super_secret.txt"
with open(file_name, "w") as file:
    file.write(super_secret_info)

# Change the permissions of the file to read-only for the owner
os.chmod(file_name, 0o400)  # Owner has read-only permission (400 in octal)

# Print the name of the file to the screen
print("Super secret file:", file_name)