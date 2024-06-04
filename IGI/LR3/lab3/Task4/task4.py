# Lab 2: Text Analysis
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

def analyze_text(text):
    """
    Analyzes the given text according to the specified requirements.
    """
    # To lower case.
    text = text.lower()

    # Split into words
    words = text.split()

    # a) Words quantity in a string.
    word_count = len(words)
    print(f"Total number of words: {word_count}")

    # b) Finding the longest word and its index.
    longest_word = max(words, key=len)
    longest_word_index = words.index(longest_word) + 1  # Words indexes start from 1
    print(f"Longest word: '{longest_word}', Index: {longest_word_index}")

    # c) Output every even word.
    even_words = [word for index, word in enumerate(words, start=1) if index % 2 == 0]
    print("Even words:")
    for word in even_words:
        print(word)


def main_4():
    """
    Main function to run the program.
    """
    # Text
    text = ("So she was considering in her own mind, as well as she could, for the hot day made her feel very sleepy "
            "and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and "
            "picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her.")

    # Text analysis
    analyze_text(text)