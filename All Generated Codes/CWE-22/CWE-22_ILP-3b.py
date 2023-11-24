import zipfile
import os

# Specify the path to the zip file
zip_file_path = 'archive.zip'

# Specify the directory where you want to extract the contents
extract_dir = '/tmp/unpack/'

# Create the extraction directory if it doesn't exist
os.makedirs(extract_dir, exist_ok=True)

try:
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Files extracted successfully to:", extract_dir)
except Exception as e:
    print("Error: ", e)