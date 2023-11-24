import tarfile
import os

# Path to the archive file
archive_file = 'archive.tar'

# Directory where you want to unpack the contents
unpack_directory = '/tmp/unpack/'

# Check if the destination directory exists, and create it if not
if not os.path.exists(unpack_directory):
    os.makedirs(unpack_directory)

try:
    # Open the archive file
    with tarfile.open(archive_file, 'r') as archive:
        # Extract all the contents to the specified directory
        archive.extractall(path=unpack_directory)
    
    print(f'Contents of {archive_file} have been successfully unpacked to {unpack_directory}')
except Exception as e:
    print(f'Error: {e}')
