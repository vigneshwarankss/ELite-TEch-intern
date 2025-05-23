import hashlib
import os
import json


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None


def save_hashes(directory, hash_file="hashes.json"):
    """Save the hash values of all files in the directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_hash(file_path)

    with open(hash_file, "w") as f:
        json.dump(file_hashes, f, indent=4)
    print("Hashes saved successfully.")


def check_integrity(directory, hash_file="hashes.json"):
    """Check file integrity by comparing stored and current hash values."""
    try:
        with open(hash_file, "r") as f:
            stored_hashes = json.load(f)
    except FileNotFoundError:
        print("No hash file found. Please generate hashes first.")
        return

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            stored_hash = stored_hashes.get(file_path)

            if stored_hash is None:
                print(f"[NEW FILE] {file_path} was added.")
            elif current_hash != stored_hash:
                print(f"[MODIFIED] {file_path} has been changed!")

    for file_path in stored_hashes.keys():
        if not os.path.exists(file_path):
            print(f"[DELETED] {file_path} is missing!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="File Integrity Checker")
    parser.add_argument("directory", help="Directory to monitor")
    parser.add_argument("--save", action="store_true", help="Save hash values of files")
    parser.add_argument("--check", action="store_true", help="Check file integrity")
    args = parser.parse_args()

    if args.save:
        save_hashes(args.directory)
    elif args.check:
        check_integrity(args.directory)
    else:
        print("Please specify either --save or --check.")
