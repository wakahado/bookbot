def get_book_text(book: str):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

def count_words(lst):
    num = 0
    for words in lst:
        num += 1
    return num 

def count_characters(str):
    dict = {}
    str = str.lower()
    for i in range(len(str) - 1):
        if str[i] not in dict:
            dict[str[i]] = 1
        else:
            dict[str[i]] += 1
    return dict

def sort_on(items: tuple[str, int]) -> int:
    return items[1]

def chars_dict_to_sorted_list(dict: dict[str, int]) -> list[tuple[str, int]]:
    sorted_lst = []
    for key, value in dict.items():
        sorted_lst.append((key, value))
    sorted_lst.sort(reverse = True, key = sort_on)
    return sorted_lst

        