import argparse

def main():
    parser = argparse.ArgumentParser(description='Data Converter')
    parser.add_argument('input_file', type=str, help='Input file path')
    parser.add_argument('output_file', type=str, help='Output file path')
    args = parser.parse_args()

    print(f'Input file: {args.input_file}')
    print(f'Output file: {args.output_file}')

if __name__ == '__main__':
    main()
