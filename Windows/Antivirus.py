import os
import hashlib

# Define the scope of the scanner
SCAN_PATHS = ['C:\\', 'D:\\']
FILE_TYPES = ['.exe', '.dll', '.sys', '.bat']

# Define the malware signature database
MALWARE_HASHES = [
    'c95aa409b6d299c0298d3a8e9b71cd97', # Trojan.GenericKD.30132277
    '0bfcf643e67928cc09e202d840d220f2', # W32.Sality.AE
    '026f8c2f58ebcac4f6fae1d1722d1e3e'  # Worm.Autorun.VHG
]

def scan_file(file_path):
    # Compute the hash value of the file
    with open(file_path, 'rb') as f:
        file_content = f.read()
    file_hash = hashlib.md5(file_content).hexdigest()
    
    # Check if the hash value matches any known malware
    if file_hash in MALWARE_HASHES:
        print(f'Found malware: {file_path}')
        # Implement a quarantine or removal mechanism here

def scan_files():
    # Search for files in the specified locations
    for scan_path in SCAN_PATHS:
        for root, dirs, files in os.walk(scan_path):
            for file_name in files:
                if any(file_name.endswith(file_type) for file_type in FILE_TYPES):
                    file_path = os.path.join(root, file_name)
                    scan_file(file_path)

if __name__ == '__main__':
    scan_files()
