import sys
from stats import count_doc_words, count_by_letter, sort_by_letter, letter_report

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_location = sys.argv[1]
    doc = get_doc_text(file_location)
    word_count = count_doc_words(doc)
    char_count = count_by_letter(doc)
    char_count.sort(key=sort_by_letter)
    letter_report(file_location,word_count,char_count)

def get_doc_text(file_location):
    with open(file_location) as f:
        contents = f.read()
    return contents
main()