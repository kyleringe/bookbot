#gives word count
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    char_counts = {}
    
    for char in text:
        lower_char = char.lower()

        if lower_char in char_counts:
            char_counts[lower_char] = char_counts[lower_char] + 1
        else:
            char_counts[lower_char] = 1
    return char_counts


def sorted_list(char_counts):
    sorted_char = []
    def sort_on(item):
        return item["num"]
    for key, value in char_counts.items():
        sorted_char.append({"char": key, "num": value})

    sorted_char.sort(reverse=True, key=sort_on)

    return sorted_char