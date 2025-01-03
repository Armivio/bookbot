def count_words(text):
    words = text.split()
    return len(words)

def read_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_characters(text):
    text = text.lower()
    counted = {}
    for char in text:
        if char.isalpha():
            if char in counted:
                counted[char] += 1
            else:
                counted[char] = 1
    return counted

def sort_on(dict):
    return dict["num"]

def print_report(words, char_list):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words} words found in the document")
    print('\n')
    for char in char_list:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print('\n')
    print("--- End report ---")

def main():
    file_contents = read_text("books/frankenstein.txt")
    # print(file_contents)
    #print(count_words(file_contents))
    #print(count_characters(file_contents))
    char_dict = count_characters(file_contents)

    # transforms dictionary into list of dictionaries:
    char_list = [{"char": char, "num": count} for char, count in char_dict.items()] 

    char_list.sort(reverse=True, key=sort_on)
    words = count_words(file_contents)
    print_report(words, char_list)
    #print(char_list)
    #print(char_list[0]["num"])


main()
