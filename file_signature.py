from constants import FILE_SIGNATURES

def get_file_extension(file_path):
    """
    Determines the file extension by reading the file's magic number (signature).

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The determined file extension or 'unknown' if the file type is not recognized.
    """
    with open(file_path, 'rb') as file:
        # Read first few bytes of the file as this is where the file signature is typically located
        file_header = file.read(8)

        # Iterate over a dict of common file signatures to compare to known values.
        for signature, extension in FILE_SIGNATURES.items():
            if file_header.startswith(signature):
                return extension
            
        return 'unknown'