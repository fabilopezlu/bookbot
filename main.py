import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

from stats import get_num_words, count_characters, create_report

def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    frankenstein_txt = get_book_text(sys.argv[1])
    #get_num_words(frankenstein_txt)
    #count_characters(frankenstein_txt)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    create_report(frankenstein_txt)
    print("============= END ===============")
main()