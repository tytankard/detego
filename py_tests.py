import pytest
from file_reconstructor import reconstruct_file, hash_file, get_file_extension
from constants import OUTPUT_FILE, FILE_PREFIX, FOLDER_PATH, HASH_HEX, COMPARISON_FILE, INCOMPLETE_FILE_NAME

# Constants
INCOMPLETE_FOLDER_PATH = f"{FOLDER_PATH}_incomplete"
MISSING_FOLDER_PATH = f"{FOLDER_PATH}_missing"

def validate_file_contents(file1, file2):
    """Check if the contents of two files are identical."""
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        contents1 = f1.read()
        contents2 = f2.read()
    return contents1 == contents2

def test_file_hash():
    """Hashes and verifies the hash_hex for a reconstructed file."""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    assert validate_file_contents(OUTPUT_FILE, COMPARISON_FILE), "File contents of reconstructed file do not match expected value"
    assert hash_file(OUTPUT_FILE) == HASH_HEX, "Hash does not match the expected value"

def test_file_type():
    """Verifies the file type of the reconstructed file."""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE, FOLDER_PATH)
    assert get_file_extension(OUTPUT_FILE) == "png", "The reconstructed file is not of type 'png'"

def test_incomplete_hash():
    """Reconstructs an incomplete file and verifies its hash."""
    reconstruct_file(FILE_PREFIX, INCOMPLETE_FILE_NAME, INCOMPLETE_FOLDER_PATH)
    assert hash_file(INCOMPLETE_FILE_NAME) != HASH_HEX, "Hash matches the expected value for a complete file"
    assert not validate_file_contents(INCOMPLETE_FILE_NAME, COMPARISON_FILE), "File contents of reconstructed file incorrectly match the comparison"

def test_missing_file():
    """Attempts to open a non-existent file and expects a FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        reconstruct_file(FILE_PREFIX, OUTPUT_FILE, MISSING_FOLDER_PATH)