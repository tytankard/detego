from file_reconstructor import FILE_PREFIX, OUTPUT_FILE, reconstruct_file, hash_file
HASH_HEX = "bd32dd329aef54c6e672089c5e301baf4b4600ed"

def test_file_hash():
    """Hashes and verifies the hash_hex for a reconstructed file"""
    reconstruct_file(FILE_PREFIX, OUTPUT_FILE)
    hash_hex = hash_file(OUTPUT_FILE)
    assert hash_hex == HASH_HEX