from stats import word_count
from stats import letter_count
from stats import sorted_list
import sys

#grabs text from a file
def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    book_text = get_book_text(path)

    num_words = word_count(book_text)

    count = letter_count(book_text)

    sorted_counts = sorted_list(count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for item in sorted_counts:
        if item["char"].isalpha():
            print(
                f"{item['char']}: {item['num']}"
            )
    print("============= END ===============")


if __name__ == "__main__":
    main()