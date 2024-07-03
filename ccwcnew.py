import argparse

def count_lines(file_content):
    return file_content.count('\n')

def count_words(file_content):
    return len(file_content.split())

def count_chars(file_content):
    return len(file_content)

def main():
    parser = argparse.ArgumentParser(description="Python clone of the wc command")
    
    parser.add_argument('files', metavar='FILE', type=str, nargs='+',
                        help='File(s) to be processed')
    parser.add_argument('-l', '--lines', action='store_true',
                        help='print the newline counts')
    parser.add_argument('-w', '--words', action='store_true',
                        help='print the word counts')
    parser.add_argument('-c', '--chars', action='store_true',
                        help='print the character counts')
    
    args = parser.parse_args()
    
    for file_name in args.files:
        try:
            with open(file_name, 'r') as file:
                content = file.read()
                
                line_count = count_lines(content)
                word_count = count_words(content)
                char_count = count_chars(content)
                
                output = []
                
                if args.lines:
                    output.append(str(line_count))
                if args.words:
                    output.append(str(word_count))
                if args.chars:
                    output.append(str(char_count))
                
                if not (args.lines or args.words or args.chars):
                    # If no specific flags are provided, default to lines, words, and chars
                    output = [str(line_count), str(word_count), str(char_count)]
                
                output.append(file_name)
                print(' '.join(output))
        
        except FileNotFoundError:
            print(f"wc: {file_name}: No such file or directory")

if __name__ == "__main__":
    main()
