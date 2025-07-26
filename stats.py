def count_doc_words(doc):
    words=doc.split()
    count = len(words)
    return count

def count_by_letter(doc):
    doc_lower = doc.lower()
    char_count = {}
    for char in doc_lower:
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in char_count:
                char_count[char]["num"] += 1
            else:
                char_count[char] = {"char": char, "num": 1}
    letter_list = list(char_count.values())
    return letter_list

def sort_by_letter(dict):
    return dict["char"]

def letter_report(file_location,word_count,sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_location}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in sorted_list:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")
    