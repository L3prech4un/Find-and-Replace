#!/usr/bin/env python3
"""
find_and_replace.py - Processes input data, finding and replacing given strings.

Usage:
    ./find_and_replace.py <filename> <find> <replace> [output_file]
    ./find_and_replace -h | --help

Arguments:
    filename        Path to input file (required)
    find            String that you want replace with <replace> (required)
    replace         String that you want to replace <find> with (required)
    output_path     Path to save results (optional, defaults to stdout)

Options:
    -h, --help      Show this help message and exit

Example:
    ./find_and_replace.py message.txt hi goodbye results.txt

Author:
    L3prech4un - https://github.com/L3prech4un
"""

import sys
import re
import os

def usage(exit_code=0):
    stream = sys.stdout if exit_code == 0 else sys.stderr
    print(__doc__.strip(), file=stream)
    sys.exit(exit_code)

def replace_word(filename: str, find: str, replace: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    
    pattern = rf"\b{re.escape(find)}\b"
    return re.sub(pattern, replace, content)

def main():
    args = sys.argv[1:]

    if any(arg in ("-h", "--help") for arg in args):
        usage(0)

    if not (3 <= len(args) <= 4):
        print("Error: Expected 3 or 4 arguments.\n", file=sys.stderr)
        usage(1)

    filename = args[0]
    find, replace = args[1], args[2]
    replaced_text = replace_word(filename, find, replace)

    if len(args) == 4:
        output_path = args[3]
        if os.path.isdir(output_path):
            print("Error: Path points to a directory, not a file.")
        else:
            try:
                with open(output_path, "w", encoding="utf-8") as outfile:
                    outfile.write(replaced_text)
                print(f"Success: Output written to {output_path}")
            except (OSError, ValueError) as e:
                print(f"Invalid path or missing parent directory: {e}")
    else:
        print(replaced_text)

if __name__ == "__main__":
    main()
