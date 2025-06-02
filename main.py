from stats import get_text_word_count
from stats import get_book_text

def main ():
    """
    Main function to execute the script.
    """
    path_to_file = 'books/frankenstein.txt'  # Replace with your file path
    book_text = get_book_text(path_to_file)
    print(book_text)
    print(get_text_word_count(book_text), "words found in the document")

if __name__ == "__main__":
    main()
