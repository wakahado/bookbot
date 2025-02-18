# print("hello world")

def count_words():
     with open("books/frankenstein.txt") as f:
         file_contents = f.read()
         words = file_contents.split()
         return(len(words))

def count_characters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    lowered_string = file_contents.lower()
   
    char_count = {} 
#用迴圈去count每一個字(char)的數目
    for char in lowered_string:
        char_count[char] = char_count.get(char, 0) + 1
    
    filterd_char_count = {k: v for k,v in char_count.items() if k.isalpha()}
    sorted_data = dict(sorted(filterd_char_count.items(), key=lambda x: x[1], reverse=True))

    for k, v in sorted_data.items():
        print(f"The '{k}' character was found {v} times")



# Report 

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count_words()} words found in the document\n")
count_characters()

print("--- End report ---")
