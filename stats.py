def get_book_text(book):
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

def sorted_list(dict):
    sorted_lst = []
    for key, value in dict.items():
        sorted_lst.append({"char": key, "num": value})
    return sorted_lst

def sort_on(items):
    return items["num"]

def sorted_character(sorted_lst):
    return sorted_lst.sort(reverse = True, key = sort_on)

        