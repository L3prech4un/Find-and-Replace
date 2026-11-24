# find_and_replace.py

Processes input data, finding and replacing given strings.

## Usage:
    ./find_and_replace.py <filename> <find> <replace> [output_file]
    ./find_and_replace -h | --help

## Arguments:
    filename        Path to input file (required)
    find            String that you want replace with <replace> (required)
    replace         String that you want to replace <find> with (required)
    output_path     Path to save results (optional, defaults to stdout)

## Options:
    -h, --help      Show this help message and exit

## Example:
    ./find_and_replace.py message.txt hi goodbye results.txt

## Author:
    L3prech4un - https://github.com/L3prech4un
