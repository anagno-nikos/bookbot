from stats import num_of_words, count_of_chars, get_ordered_char_dict
import sys

def get_book_text(filepath: str, ) -> str:
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main() -> None:
    words = get_book_text(sys.argv[1])
    num_words = num_of_words(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_dict = count_of_chars(words)
    print("--------- Character Count -------")
    ordered_dict_char_count = get_ordered_char_dict(chars_dict)       
    for char_dict in ordered_dict_char_count:
        if char_dict["char"].isalpha():
            print(f"{char_dict['char']}: {char_dict['num']}")
    print("============= END ===============")


if len(sys.argv) == 2:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
