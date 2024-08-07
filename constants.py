
FILE_PREFIX = "part"
OUTPUT_FILE = "reconstructed_file"
FOLDER_PATH = "SplitFile"

FILE_SIGNATURES = {
    b'\xFF\xD8\xFF': 'jpg',
    b'\x89PNG\r\n\x1A\n': 'png',
    b'GIF87a': 'gif',
    b'GIF89a': 'gif',
    b'\x25PDF': 'pdf',
    b'\x50\x4B\x03\x04': 'zip',
    b'\x49\x49\x2A\x00': 'tif',
    b'\x4D\x4D\x00\x2A': 'tif',
    b'\x00\x00\x01\x00': 'ico',
    b'\x52\x49\x46\x46': 'webp',
    b'OggS': 'ogg',
    b'fLaC': 'flac',
    b'ID3': 'mp3',
    b'\x42\x4D': 'bmp'
    # Add more signatures as needed
}