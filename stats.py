def get_num_words(input_text):
    word_array = input_text.split()
    num_words = len(word_array)
    #print(f"{num_words} words found in the document")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

def count_characters(input_text):
    char_dict = {}
    input_text = input_text.lower()
    for character in input_text:
        if character in char_dict:
            char_dict[character] += 1
        else:
            char_dict[character] = 1
    #print(char_dict)
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(char_dict):
    list_of_dicts = []
    for character, count in char_dict.items():
        doubled_dict = {'char': character, 'num': count}
        list_of_dicts.append(doubled_dict)
    list_of_dicts.sort(reverse=True, key=sort_on)
    print("--------- Character Count -------")
    for dict in list_of_dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")

def create_report(book):
    get_num_words(book)
    char_dict = count_characters(book)
    sort_dict(char_dict)
    