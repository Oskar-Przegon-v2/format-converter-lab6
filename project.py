import argparse
import json
import os

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Data Converter')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} does not exist.')
        return

    if not args.input_file.endswith('.json'):
        print(f'Error: Input file must be a .json file.')
        return

    if not args.output_file.endswith('.json'):
        print(f'Error: Output file must be a .json file.')
        return

    try:
        data = read_json(args.input_file)
        print(f'Loaded data: {data}')
        write_json(data, args.output_file)
        print(f'Data saved to {args.output_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
