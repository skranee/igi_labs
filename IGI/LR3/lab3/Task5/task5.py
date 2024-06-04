# Lab 2: Real Number List Processing
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

import random
import time


def timing_decorator(func):
    """
    Timer decorator function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time of function execution '{func.__name__}': {end_time - start_time} seconds.")
        return result
    return wrapper


def generate_random_array(length, min_value, max_value):
    """
    Generating random array of length = {length} and filling it
    with integers of value {min_value} to {max_value}
    """
    count = 1
    while count <= length:
        yield count
        count = random.uniform(min_value, max_value)


@timing_decorator
def input_list():
    """
    Function allowing input of numbers list.
    """
    while True:
        try:
            elements = input("Enter the elements of the list separated by spaces: ").split()
            elements = [float(element) for element in elements]
            return elements
        except ValueError:
            print("Error: Please enter valid real numbers separated by spaces.")


def validate_input(elements):
    """
    Validates the input list.
    """
    if len(elements) < 2:
        print("Error: List should contain at least 2 elements.")
        return False
    return True


def process_list(elements):
    """
    Processes the input list.
    """
    negative_sum = sum(element for element in elements if element < 0)

    if elements:
        max_index = elements.index(max(elements))
        min_index = elements.index(min(elements))
        start_index, end_index = min(max_index, min_index), max(max_index, min_index)
        multiplication = 1
        if end_index - start_index > 1:
            multiplication = 1
            for element in elements[start_index + 1:end_index]:
                multiplication *= element
    else:
        multiplication = 0

    return negative_sum, multiplication


def print_list(elements):
    """
    Prints the list of elements.
    """
    print("List of elements:", elements)


def decide_method():
    """
    Allows user to choose which method of array filling is going to be used.
    """
    while True:
        try:
            fill_choice = input('\nChoose how to fill the array (1 - on your own, 2 - automatically): ')
            return int(fill_choice)
        except ValueError:
            print("Error: Please enter a number.")


def main_5():
    """
    Main function to run the program.
    """
    while True:

        fill_choice = decide_method()

        if fill_choice == 1:
            # List input for the user.
            elements = input_list()
        else:
            # List input automatically.
            elements = generate_random_array(15, -50, 50)

        # Validation.
        if not validate_input(elements):
            return

        # List handler.
        negative_sum, product = process_list(elements)

        # Result output.
        print("Sum of negative elements:", negative_sum)
        print("Multiplied elements between max and min:", product)

        # List output.
        print_list(elements)

        choice = input("Do you want to run the program again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the program.")
            break
