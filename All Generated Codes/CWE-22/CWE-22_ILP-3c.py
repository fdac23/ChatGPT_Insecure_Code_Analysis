import tarfile

# Define the path to the TAR archive
tar_file_path = 'example.tar.gz'

# Specify the target directory where you want to extract the files
target_directory = 'extracted_files/'

# Create a context manager using the 'tarfile.open' method
with tarfile.open(tar_file_path, 'r:gz') as tar:
    # List the contents of the TAR archive
    tar.list()

    # Extract all files from the archive to the specified target directory
    tar.extractall(target_directory)

# The 'with' statement ensures that the TAR archive is properly closed after the block
print("Files extracted to:", target_directory)