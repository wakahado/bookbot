from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    print("Missing a file name!")
    sys.exit(1)

book = sys.argv[1]
lst = get_book_text(book).split()
word_counts = count_words(lst)

str = get_book_text(book)
dict = count_characters(str)
sorted_lst = chars_dict_to_sorted_list(dict)

def print_report(book, word_counts, sorted_lst):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_lst) - 1):
        if sorted_lst[i][0].isalpha():
            print(f"{sorted_lst[i][0]}: {sorted_lst[i][1]}\n")
    print("============= END ===============")

print_report(book, word_counts, sorted_lst)
