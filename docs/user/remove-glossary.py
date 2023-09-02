import os
import re

def find_rst_files(start_dir):
    rst_files = []
    for root, dirs, files in os.walk(start_dir):
        for file in files:
            if file.endswith(".rst"):
                rst_files.append(os.path.join(root, file))
    return rst_files

def replace_terms(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace :term:`texto` with texto using regular expressions
    new_content = re.sub(r':term:`(.*?)`', r'\1', content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    start_directory = '.'  # Starting directory ('.' refers to the current directory)
    rst_files = find_rst_files(start_directory)

    for rst_file in rst_files:
        print(f"Processing {rst_file}...")
        replace_terms(rst_file)
        print(f"Done processing {rst_file}")

if __name__ == "__main__":
    main()
