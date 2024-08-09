import argparse
from os import path
from file_reconstructor import reconstruct_file, hash_file, get_file_extension, write_file_with_extension

def cli():
    parser = argparse.ArgumentParser(description="Reconstruct a file from split parts and optionally hash it.")
    
    parser.add_argument(
        '-f', '--folder',
        type=str,
        required=True,
        help="Path to the folder containing the split files."
    )
    
    parser.add_argument(
        '-p', '--prefix',
        type=str,
        required=True,
        help="Prefix used in the split filenames (e.g., 'part' for 'part_1', 'part_2', etc.)."
    )
    
    parser.add_argument(
        '-o', '--output',
        type=str,
        required=True,
        help="Name of the output file to be reconstructed."
    )
    
    parser.add_argument(
        '-v', '--verify',
        action='store_true',
        help="Verify the reconstructed file by computing its SHA-1 hash."
    )

    args = parser.parse_args()
    
    # Ensure the folder exists
    if not path.exists(args.folder):
        print(f"Error: The folder '{args.folder}' does not exist.")
        return
    
    # Reconstruct the file
    try:
        reconstruct_file(args.prefix, args.output, args.folder)
        extension = get_file_extension(args.output)
        write_file_with_extension(args.output, extension)
        print(f"File '{args.output}' has been successfully reconstructed.")
    except Exception as e:
        print(f"An error occurred during file reconstruction: {str(e)}")
        return

    # Optionally verify the file
    if args.verify:
        try:
            hashed_hex = hash_file(args.output)
            print(f"SHA-1 hash of the file '{args.output}': {hashed_hex}")
        except Exception as e:
            print(f"An error occurred during file hashing: {str(e)}")

if __name__ == "__main__":
    cli()