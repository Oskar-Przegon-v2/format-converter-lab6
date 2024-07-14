import argparse
import json
import xmltodict
import yaml
import os

def read_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_xml(file_path):
    with open(file_path, 'r') as file:
        data = xmltodict.parse(file.read())
    return data

def write_xml(data, file_path):
    data = {"root": data}
    with open(file_path, 'w') as file:
        file.write(xmltodict.unparse(data, pretty=True))


def read_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

def write_yaml(data, file_path):
    with open(file_path, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def read_file(file_path):
    if file_path.endswith('.json'):
        return read_json(file_path)
    elif file_path.endswith('.xml'):
        return read_xml(file_path)
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return read_yaml(file_path)
    else:
        raise ValueError('Unsupported file format')

def write_file(data, file_path):
    if file_path.endswith('.json'):
        write_json(data, file_path)
    elif file_path.endswith('.xml'):
        write_xml(data, file_path)
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        write_yaml(data, file_path)
    else:
        raise ValueError('Unsupported file format')

def main():
    parser = argparse.ArgumentParser(description='Data Converter')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    args = parser.parse_args()

    if not os.path.exists(args.input_file):
        print(f'Error: Input file {args.input_file} does not exist.')
        return

    supported_formats = ['.json', '.xml', '.yml', '.yaml']
    if not any(args.input_file.endswith(ext) for ext in supported_formats):
        print(f'Error: Unsupported input file format. Supported formats are: {supported_formats}')
        return

    if not any(args.output_file.endswith(ext) for ext in supported_formats):
        print(f'Error: Unsupported output file format. Supported formats are: {supported_formats}')
        return

    try:
        data = read_file(args.input_file)
        write_file(data, args.output_file)
        print(f'Data converted and saved to {args.output_file}')
    except Exception as e:
        print(f'Error: {e}')

if __name__ == '__main__':
    main()
