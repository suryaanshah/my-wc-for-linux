import argparse
import subprocess

def count_lines(file_content):
    return file_content.count(b'\n')

def count_paras(file_content):
    return file_content.count(b'\n\n')

def count_words(file_content):
    return len(file_content.split())

def count_bytes(file_content):
    return len(file_content)

def main():
    parser = argparse.ArgumentParser(description="Python clone of the wc command")
    
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                        help='File(s) to be processed')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true',
                        help='print the word counts')
    parser.add_argument('-c', '--bytes', action='store_true',
                        help='print the byte counts')
    
    args = parser.parse_args()
    
    for file_name in args.files:
        try:
            with open(file_name, 'rb') as file:  # Read the file in binary mode
                content = file.read()
                
                line_count = count_lines(content)
                word_count = count_words(content)
                byte_count = count_bytes(content)
                
                output = []
                
                if args.lines:
                    output.append(str(line_count))
                if args.words:
                    output.append(str(word_count))
                if args.bytes:
                    output.append(str(byte_count))
                
                if not (args.lines or args.words or args.bytes):
                    output = [str(line_count), str(word_count), str(byte_count)]
                
                output.append(file_name)
                print(' '.join(output))
        
        except FileNotFoundError:
            print(f"wc: {file_name}: No such file or directory")

if __name__ == "__main__":
    main()
