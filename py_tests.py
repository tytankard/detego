import pytest
from file_reconstructor import FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH, reconstruct_file, hash_file
HASH_HEX = "bd32dd329aef54c6e672089c5e301baf4b4600ed"
COMPARISON_FILE = "comparison_file"

def validate_file_contents(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        contents1 = f1.read()
        contents2 = f2.read()
    return contents1 == contents2 
    
def test_file_hash():
    """Hashes and verifies the hash_hex for a reconstructed file"""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    contents_match = validate_file_contents
    hash_hex = hash_file(OUTPUT_FILE)
    assert hash_hex == HASH_HEX, "Value does not match the correctly expected hash"
    assert contents_match, "File contents of reconstructed file does not match expected value"

def test_incomplete_hash():
    """Reconstructs and icomplete file and tries to hash"""
    reconstruct_file(FILE_PREFIX, 'incomplete.png', f"{FOLDER_PATH}_incomplete")
    hash_hex = hash_file('incomplete.png')
    assert hash_hex != HASH_HEX, "Value does not match the correctly expected hash"

def test_missing_file():
    """Tries to open a file that does not exist"""
    with pytest.raises(FileNotFoundError):
        print(f"{FOLDER_PATH}_missing")
        reconstruct_file(FILE_PREFIX, OUTPUT_FILE, f"{FOLDER_PATH}_missing")