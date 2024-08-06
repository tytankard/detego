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
    items = listdir(folder)
    files_len = len([item for item in items if path.isfile(path.join(folder, item))])
    print(f"Output = {output}")
    if path.exists(output):
        print("File already exists - deleting existing file before continuing")
        try:
            remove(output)
            print(f"File {output} deleted successfully.")
        except OSError as e:
            print(f"Error: {e.strerror}")

    with open(output, 'wb') as output_file:
        for i in range(1, files_len + 1):
            file_name = f"{prefix}_{i}"
            if path.exists(f"{folder}/{file_name}"):
                with open(f"{folder}/{file_name}", 'rb') as file:
                    output_file.write(file.read())
            else:
                raise FileNotFoundError

def hash_file(file_name):
    hash_obj = sha1()
    with open(file_name, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    status = main()
    print(status)