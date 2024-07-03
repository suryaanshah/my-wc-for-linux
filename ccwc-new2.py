import argparse

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
