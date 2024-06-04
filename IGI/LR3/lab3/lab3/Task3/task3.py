# Lab 2: Count Uppercase Letters
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

def count_uppercase_letters():
    """
    Counts the number of uppercase English letters in a string.
    """
    try:
        user_input = input("Enter a string: ")
        count = sum(1 for char in user_input if char.isupper() and char.isalpha())
        return count
    except Exception as e:
        print("Error:", e)
        return 0


def main_3():
    """
    Main function to run the program.
    """
    while True:
        count = count_uppercase_letters()
        print(f"Number of uppercase letters: {count}")
        choice = input("Do you want to count again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the program.")
            break
