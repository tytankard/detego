from os import listdir, path
from hashlib import sha1

FILE_PREFIX = "part"
OUTPUT_FILE = "reconstructed_file"
FOLDER_PATH = "SplitFile"

def main():
    hashed_hex = hash_file(OUTPUT_FILE)
    return(f"File: {OUTPUT_FILE} succesfully hashed with hex: {hashed_hex}")

def reconstruct_file(prefix, output):
    items = listdir(FOLDER_PATH)
    files_len = len([item for item in items if path.isfile(path.join(FOLDER_PATH, item))])

    with open(output, 'wb') as output_file:
        for i in range(1, files_len + 1):
            file_name = f"{FILE_PREFIX}_{i}"
            with open(f"{FOLDER_PATH}/{file_name}", 'rb') as file:
                output_file.write(file.read())

def hash_file(file_name):
    hash_obj = sha1()
    with open(file_name, 'rb') as f:
        while chunk := f.read(8192):
            hash_obj.update(chunk)
    return hash_obj.hexdigest()

if __name__ == '__main__':
    status = main()
    print(status)