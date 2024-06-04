# Lab 2: Sum of Squares
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

import math


def sum_of_squares():
    """
    Computes the sum of squares of integers entered by the user until 0 is entered.
    """
    total = 0
    try:
        while True:
            num = int(input("Enter an integer (0 to end): "))
            if num == 0:
                break
            total += int(math.pow(num, 2))
    except ValueError:
        print("Error: Please enter valid integers.")

    return total


def main_2():
    """
    Main function to run the program.
    """
    while True:
        result = sum_of_squares()
        print(f"Sum of squares: {result}")
        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the program.")
            break