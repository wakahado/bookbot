from stats import *
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    print("Missing a file name!")
    sys.exit(1)

book = sys.argv[1]
lst = get_book_text(book).split()
str = get_book_text(book)
dict = count_characters(str)
sorted_lst = sorted_list(dict)


def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(lst)} total words")
    print("--------- Character Count -------")
    sorted_character(sorted_lst)
    for i in range(len(sorted_lst) - 1):
        print(f"{sorted_lst[i]['char']}: {sorted_lst[i]['num']}\n")
    print("============= END ===============")

main()
