# Lab 4: Text Analyzer
# Version 1.0
# Developer: Abmetko Pavel
# Date: 04.13.2024

import re
import zipfile


class TextAnalyzerMixin:
    """
    A mixin class containing common text analysis methods.
    """

    def find_uppercase_english_letters(self, text):
        """
        Find all uppercase English letters in the text.

        Args:
            text (str): The text to search for uppercase letters.

        Returns:
            list: A list of uppercase English letters found in the text.
        """
        uppercase_letters = re.findall(r'[A-Z]', text)
        return uppercase_letters

    def replace_complex_sequence(self, text):
        """
        Replace the complex sequence 'a...ab...bc...c' with 'qqq' in the text.

        Args:
            text (str): The text to perform replacement.

        Returns:
            str: The text after performing the replacement.
        """
        replaced_text1 = re.sub(r'ab', 'qqq', text)
        replaced_text2 = re.sub(r'bc', 'qqq', replaced_text1)
        return replaced_text2

    def count_sentences(self, text):
        """
        Count the number of sentences in the text.

        Args:
            text (str): The text to count sentences.

        Returns:
            int: The number of sentences in the text.
        """
        sentences = re.split(r'[.!?]+', text)
        return len(sentences) - 1

    def count_sentence_types(self, text):
        """
        Count the number of sentences of each type (declarative, interrogative, imperative) in the text.

        Args:
            text (str): The text to count sentence types.

        Returns:
            dict: A dictionary containing the counts of each sentence type.
        """
        sentence_types = {
            "declarative": 0,
            "interrogative": 0,
            "imperative": 0
        }

        for char in text:
            if char == '?':
                sentence_types["interrogative"] += 1
            elif char == '.':
                sentence_types["declarative"] += 1
            elif char == '!':
                sentence_types["imperative"] += 1

        return sentence_types

    def average_sentence_length(self, text):
        """
        Calculate the average sentence length in characters (word length).

        Args:
            text (str): The text to calculate average sentence length.

        Returns:
            float: The average sentence length in characters.
        """
        words = re.findall(r'\b\w+\b', text)
        total_characters = sum(len(word) for word in words)
        total_sentences = self.count_sentences(text)
        return total_characters / total_sentences if total_sentences > 0 else 0

    def average_word_length(self, text):
        """
        Calculate the average word length in characters.

        Args:
            text (str): The text to calculate average word length.

        Returns:
            float: The average word length in characters.
        """
        words = re.findall(r'\b\w+\b', text)
        total_characters = sum(len(word) for word in words)
        total_words = len(words)
        return total_characters / total_words if total_words > 0 else 0

    def count_smileys(self, text):
        """
        Count the number of smileys in the text.

        Args:
            text (str): The text to count smileys.

        Returns:
            int: The number of smileys in the text.
        """
        smiley_pattern = r'[;:]-*[\(\[\)\]]+'
        smileys = re.findall(smiley_pattern, text)
        return len(smileys)

    def find_longest_word_ending_with_e(self, text):
        """
        Find the longest word in the text that ends with 'e'.

        Args:
            text (str): The text to search for words.

        Returns:
            str: The longest word ending with 'e' found in the text.
        """
        words = re.findall(r'\b\w+e\b', text)
        return max(words, key=len) if words else None

    def find_max_length_words(self, text):
        """
        Find words with maximum length in the text.

        Args:
            text (str): The text to search for words.

        Returns:
            list: A list of words with maximum length found in the text.
        """
        words = re.findall(r'\b\w+\b', text)
        max_length = max(len(word) for word in words)
        return [word for word in words if len(word) == max_length]

    def find_words_followed_by_comma_or_period(self, text):
        """
        Find words followed by a comma or period in the text.

        Args:
            text (str): The text to search for words.

        Returns:
            list: A list of words followed by a comma or period found in the text.
        """
        words = re.findall(r'\b\w+(?=,|\.)(?=,|\.|$)', text)
        return words


class TextAnalyzer(TextAnalyzerMixin):
    """
    A class to perform text analysis tasks.
    """

    def __init__(self, filename):
        """
        Initialize the TextAnalyzer with the specified filename.

        Args:
            filename (str): The name of the file to analyze.
        """
        self.filename = filename
        self.text = self.read_text_from_file()

    def read_text_from_file(self):
        """
        Read text from the specified file.

        Returns:
            str: The text read from the file.
        """
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()


class TextAnalysisResults:
    """
    A class to store and process the results of text analysis.
    """

    def __init__(self):
        """
        Initialize the TextAnalysisResults instance.
        """
        self.analysis_results = []

    def add_result(self, result):
        """
        Add a result to the list of results.

        Args:
            result (str): The result to add.
        """
        self.analysis_results.append(result)

    def save_to_file(self, filename):
        """
        Save the results to a file.

        Args:
            filename (str): The name of the file to save the results to.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            for result in self.analysis_results:
                file.write(result + '\n')


class TextAnalysis(TextAnalyzer, TextAnalysisResults):
    """
    A class to perform text analysis and store results.
    """

    def __init__(self, filename):
        """
        Initialize the TextAnalysis instance.

        Args:
            filename (str): The name of the file to analyze.
        """
        try:
            super().__init__(filename)
        except FileNotFoundError:
            print("Incorrect filename")
            exit()
        self.analysis_results = []  # Initialize the analysis_results attribute

    def main(self):
        """
        Main function to execute the text analysis program.
        """
        # Perform text analysis tasks
        uppercase_letters = self.find_uppercase_english_letters(self.text)
        replaced_text = self.replace_complex_sequence(self.text)
        sentence_count = self.count_sentences(self.text)
        sentence_types_count = self.count_sentence_types(self.text)
        avg_sentence_length = self.average_sentence_length(self.text)
        avg_word_length = self.average_word_length(self.text)
        smiley_count = self.count_smileys(self.text)
        longest_word_ending_with_e = self.find_longest_word_ending_with_e(self.text)
        max_length_words = self.find_max_length_words(self.text)
        words_followed_by_comma_or_period = self.find_words_followed_by_comma_or_period(self.text)

        # Display results to the user
        print("Uppercase English letters:", uppercase_letters)
        print("Replaced text:", replaced_text)
        print("Amount of sentences:", sentence_count)
        print("Amount of declarative sentences:", sentence_types_count["declarative"])
        print("Amount of interrogative sentences:", sentence_types_count["interrogative"])
        print("Amount of imperative sentences:", sentence_types_count["imperative"])
        print("Average sentence length:", avg_sentence_length)
        print("Average word length:", avg_word_length)
        print("Amount of smileys:", smiley_count)
        print("Longest word ending with 'e':", longest_word_ending_with_e)
        print("Words with maximum length:", max_length_words)
        print("Words followed by comma or period:", words_followed_by_comma_or_period)

        # Save results to a file
        results_filename = 'analysis_results.txt'
        self.add_result(f"Uppercase English letters: {uppercase_letters}")
        self.add_result(f"Replaced text: {replaced_text}")
        self.add_result(f"Amount of sentences: {sentence_count}")
        self.add_result(f"Amount of declarative sentences: {sentence_types_count['declarative']}")
        self.add_result(f"Amount of interrogative sentences: {sentence_types_count['interrogative']}")
        self.add_result(f"Amount of imperative sentences: {sentence_types_count['imperative']}")
        self.add_result(f"Average sentence length: {avg_sentence_length}")
        self.add_result(f"Average word length: {avg_word_length}")
        self.add_result(f"Amount of smileys: {smiley_count}")
        self.add_result(f"Longest word ending with 'e': {longest_word_ending_with_e}")
        self.add_result(f"Words with maximum length: {max_length_words}")
        self.add_result(f"Words followed by comma or period: {words_followed_by_comma_or_period}")

        self.save_to_file(results_filename)

        # Archive the results file
        with zipfile.ZipFile('results.zip', 'w') as zip_file:
            zip_file.write(results_filename)

        # Provide information about the archived file
        zip_info = zipfile.ZipFile('results.zip', 'r')
        archived_files = zip_info.namelist()
        print("\nInformation about the archived file:")
        for file in archived_files:
            print(file)
        zip_info.close()


if __name__ == "__main__":
    filename = input("Enter the name of the file to analyze: ")
    analyzer = TextAnalysis(filename)
    analyzer.main()
