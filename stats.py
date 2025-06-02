def get_book_text(path_to_file):
    """
    Reads the content of a file and returns it as a string.
    
    :param path_to_file: The path to the file to be read.
    :return: The content of the file as a string.
    """
    with open(path_to_file, 'r', encoding='utf-8') as file:
        return file.read()


def get_text_word_count(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: The number of words in the text.
    """
    return len(text.split())
