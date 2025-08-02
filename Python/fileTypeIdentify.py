import os
import zipfile

# Signatures in hexadecimal for PDF, DOC, DOCX #https://en.wikipedia.org/wiki/List_of_file_signatures
file_signatures = {
    b'\x25\x50\x44\x46\x2D': 'PDF document',                 # %PDF- 
    b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1': 'Microsoft Word (.doc) document',
    b'\x50\x4B\x03\x04': 'ZIP archive (possible .docx or other ZIP files)',  # PK\x03\x04
    b'\xFF\xFE\x00\x00': 'Text File'
}

def is_docx(file_path):
    """Check if a ZIP archive contains a [Content_Types].xml file indicating a .docx"""
    try:
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            if '[Content_Types].xml' in zip_ref.namelist():
                return True
    except zipfile.BadZipFile:
        return False
    return False

def identify_file_type(file_path):
    max_signature_length = max(len(sig) for sig in file_signatures)
    try:
        with open(file_path, 'rb') as f:
            file_start = f.read(max_signature_length)
            for signature, file_type in file_signatures.items():
                if file_start.startswith(signature):
                    if signature == b'\x50\x4B\x03\x04':
                        # Check if it's a .docx
                        if is_docx(file_path):
                            print(f'file start {file_start}')
                            return 'Microsoft Word (.docx) document'
                        else:
                            return 'ZIP archive (not a .docx)'
                    elif signature == b'\x25\x50\x44\x46\x2D':
                        #print(f'file start {file_start}')
                        return 'PDF document'
                    elif signature == b'\xD0\xCF\x11\xE0\xA1\xB1\x1A\xE1':
                        #print(f'file start {file_start}')
                        return 'Microsoft Word (.doc) document'
                    elif signature == b'\xFF\xFE\x00\x00':
                        #print(f'file start {file_start}')
                        return 'Text File'
        # If no signature matches, assume plain text or unknown
        #print(f'file start {file_start}')
        return 'Unknown Signature'
    except Exception as e:
        return f'Error reading file: {e}'

def main(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_type = identify_file_type(file_path)
            print(f"{filename}: {file_type}")
            # print(f"root: {root}")
            # print(f"dirs: {dirs}")
            # print(f"files: {files}")


if __name__ == "__main__":
    dir_path = r"D:\WorkSpace\AgenticAI_POC\src\knowledge" #input("Enter the directory path: ")
    main(dir_path)