import argparse
import json

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

    try:
        data = read_json(args.input_file)
        print(f'Loaded data: {data}')
        write_json(data, args.output_file)
        print(f'Data saved to {args.output_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
