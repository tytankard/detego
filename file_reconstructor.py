import logging
from os import listdir, path
from hashlib import sha1
from constants import OUTPUT_FILE, FILE_PREFIX, FOLDER_PATH, FILE_SIGNATURES
from file_signature import get_file_extension

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
        extension = get_file_extension(OUTPUT_FILE)
        write_file_with_extension(OUTPUT_FILE, extension)
        hashed_hex = hash_file(OUTPUT_FILE)
        logging.info(f"File: {OUTPUT_FILE} successfully hashed with hex: {hashed_hex}")
        return hashed_hex
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        return None

def reconstruct_file(prefix, output, folder):
    """
    Reconstructs a file by concatenating multiple files from a specified folder.

    This function reads files from the given folder with names following the 
    pattern output_i, where i ranges from 1 to the number of files in the folder.
    These files are concatenated in order and written to the output file.

    Args:
        prefix (str): The prefix used in the filenames to reconstruct the file.
        output (str): The path to the output file where the reconstructed content will be saved.
        folder (str): The directory where the source files are located.

    Raises:
        FileNotFoundError: If any expected file with the pattern output_i does not exist in the folder.
    """
    with open(output, 'wb') as output_file:
        i = 1
        while True:
            file_name = f"{prefix}_{i}"
            file_path = path.join(folder, file_name)
            if not path.exists(file_path):
                if i == 1:
                    logging.error(f"No files found with prefix '{prefix}' in folder '{folder}'")
                    raise FileNotFoundError(f"No files found with prefix '{prefix}' in folder '{folder}'")
                break
            with open(file_path, 'rb') as file:
                for chunk in iter(lambda: file.read(8192), b''):
                    output_file.write(chunk)
            i += 1

def hash_file(file_name):
    """
    Computes the SHA-1 hash of a file.

    This function reads the file specified by file_name in binary mode and computes
    its SHA-1 hash, returning the hexadecimal representation of the hash.

    Args:
        file_name (str): The path to the file to be hashed.

    Returns:
        str: The hexadecimal SHA-1 hash of the file's contents.
    """
    hash_obj = sha1()
    with open(file_name, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

def write_file_with_extension(file_path, extension):
    """
    Writes the given file path and extension to a new file.

    Args:
        file_path (str): The path to the file.
        extension (str): The file extension.
    """
    if path.exists(file_path):
        with open(file_path, 'rb') as file:
            with open(f"{file_path}.{extension}", 'wb') as output:
                output.write(file.read())
    else:
        logging.error(f"The file '{file_path}' does not exist")
        raise FileNotFoundError(f"The file '{file_path}' does not exist")
        
if __name__ == '__main__':
    status = main()
    if status:
        logging.info(f"Process completed successfully with hash: {status}")
    else:
        logging.error("Process failed.")
