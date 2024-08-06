from os import listdir, path, remove
from hashlib import sha1

FILE_PREFIX = "part"
OUTPUT_FILE = "reconstructed_file"
FOLDER_PATH = "SplitFile"

def main():
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    hashed_hex = hash_file(OUTPUT_FILE)
    return(f"File: {OUTPUT_FILE} succesfully hashed with hex: {hashed_hex}")

def reconstruct_file(prefix, output, folder):
    """
    Reconstructs a file by concatenating multiple files from a specified folder.

    This function reads files from the given folder with names following the 
    pattern `output_i`, where `i` ranges from 1 to the number of files in the folder.
    These files are concatenated in order and written to the `output` file.

    Args:
        prefix (str): The prefix used in the filenames to reconstruct the file.
        output (str): The path to the output file where the reconstructed content will be saved.
        folder (str): The directory where the source files are located.

    Raises:
        FileNotFoundError: If any expected file with the pattern `output_i` does not exist in the folder.
    """
    items = listdir(folder)
    files_len = len([item for item in items if path.isfile(path.join(folder, item))])
    with open(output, 'wb') as output_file:
        for i in range(1, files_len + 1):
            file_name = f"{prefix}_{i}"
            if path.exists(f"{folder}/{file_name}"):
                with open(f"{folder}/{file_name}", 'rb') as file:
                    output_file.write(file.read())
            else:
                raise FileNotFoundError

def hash_file(file_name):
    """
    Computes the SHA-1 hash of a file.

    This function reads the file specified by `file_name` in binary mode and computes
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

if __name__ == '__main__':
    status = main()
    print(status)