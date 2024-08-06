import pytest
import filetype
from file_reconstructor import FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH, reconstruct_file, hash_file
HASH_HEX = "bd32dd329aef54c6e672089c5e301baf4b4600ed"
COMPARISON_FILE = "comparison_file"

def get_file_type(file_path):
    file_type = filetype.guess(file_path)
    print(f"File type = {file_type.mime}")
    return file_type

def validate_file_contents(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        contents1 = f1.read()
        contents2 = f2.read()
    return contents1 == contents2

def test_file_hash():
    """Hashes and verifies the hash_hex for a reconstructed file"""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    contents_match = validate_file_contents(OUTPUT_FILE, COMPARISON_FILE)
    hash_hex = hash_file(OUTPUT_FILE)
    assert hash_hex == HASH_HEX, "Value does not match the correctly expected hash"
    assert contents_match, "File contents of reconstructed file does not match expected value"

def test_file_type():
    """Hashes and verifies the file type"""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    file_type = get_file_type(OUTPUT_FILE)
    assert file_type.extension == "png", "The reconstructed file is not of type 'png'"
    
def test_incomplete_hash():
    """Reconstructs and icomplete file and tries to hash"""
    incomplete_file_name = 'incomplete'
    reconstruct_file(FILE_PREFIX, incomplete_file_name, f"{FOLDER_PATH}_incomplete")
    contents_match = validate_file_contents(incomplete_file_name, COMPARISON_FILE)
    hash_hex = hash_file(incomplete_file_name)
    assert hash_hex != HASH_HEX, "Value does not match the correctly expected hash"
    assert not contents_match, "File contents of reconstructed file incorrectly equals the comparison"

def test_missing_file():
    """Tries to open a file that does not exist"""
    with pytest.raises(FileNotFoundError):
        print(f"{FOLDER_PATH}_missing")#
        reconstruct_file(FILE_PREFIX, OUTPUT_FILE, f"{FOLDER_PATH}_missing")