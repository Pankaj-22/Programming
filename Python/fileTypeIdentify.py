import os
import zipfile
import string

# Known binary file signatures
FILE_SIGNATURES = {
    b'%PDF-': 'PDF document',
    b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1': 'Microsoft Word (.doc) document',
    b'PK\x03\x04': 'ZIP archive (possible .docx or other ZIP files)',
    b'\xFF\xFE\x00\x00': 'UTF-32 LE Text File'
}

def is_docx(file_path):
    """Check if ZIP archive contains [Content_Types].xml (used in .docx)"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            return '[Content_Types].xml' in zip_ref.namelist()
    except zipfile.BadZipFile:
        return False

def is_probably_text(data, threshold=0.9):
    """Returns True if most characters in data are printable (ASCII/UTF-8)"""
    if not data:
        return False
    printable_count = sum(chr(b) in string.printable or chr(b) in '\r\n\t' for b in data)
    return (printable_count / len(data)) >= threshold

def identify_file_type(file_path):
    try:
        max_len = max(len(sig) for sig in FILE_SIGNATURES)
        with open(file_path, 'rb') as f:
            file_start = f.read(max_len)

        for signature, file_type in FILE_SIGNATURES.items():
            if file_start.startswith(signature):
                if signature == b'PK\x03\x04':
                    return 'Microsoft Word (.docx) document' if is_docx(file_path) else 'ZIP archive (not a .docx)'
                return file_type

        if is_probably_text(file_start):
            return 'Text File (ASCII/UTF-8)'

        return 'Unknown Signature'
    except Exception as e:
        return f'Error reading file: {e}'

def main(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_type = identify_file_type(file_path)
            print(f"{filename}: {file_type}")

if __name__ == "__main__":
    dir_path = r"D:\WorkSpace\AgenticAI_POC\src\knowledge"  # Update if needed
    main(dir_path)
