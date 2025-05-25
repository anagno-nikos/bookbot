def sort_on(dict):
    return dict["num"]

def num_of_words(words: str) -> int:
    return len(words.split())

def count_of_chars(words: str) -> dict:
    chars_dict_count = {}
    lower_words = words.lower()
    for char in lower_words:
        if char in chars_dict_count:
            chars_dict_count[char] += 1
        else:
            chars_dict_count[char] = 1
    return chars_dict_count

def get_ordered_char_dict(character_dict):
    character_dict_detailed = []
    for k, v in character_dict.items():
        character_dict_detailed.append(
            {
                "char": k,
                "num": v,
            }
        )
    character_dict_detailed.sort(reverse=True, key=sort_on)
    return character_dict_detailed
