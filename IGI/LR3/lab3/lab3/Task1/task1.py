# Lab 2: Power Series Approximation of ln((x+1)/(x-1))
# Version 1.0
# Developer: Abmetko Pavel
# Date: 03.30.2024

import math


def ln_approximation(x, eps=1e-9, max_iter=500):
    """
    Approximates the natural logarithm of ((x+1)/(x-1)) using power series expansion.
    """
    result = 0
    for n in range(1, max_iter + 1):
        term = -((math.pow(-2, n)) * math.pow(1 / (-1 + x), n)) / n
        result += term
        if abs(term) < eps:
            break
    return result, n

# 2 / (((2 * n) + 1) * math.pow(x, ((2 * n) + 1)))

def user_interface():
    """
    Interface for interacting with the program.
    """
    try:
        x = float(input("Enter the value of x ( > 1): "))
        if abs(x) <= 1:
            print("Error: |x| should be greater than 1.")
            return

        eps = float(input("Enter precision: "))

        result, n = ln_approximation(x, eps)
        base = (x + 1) / (x - 1)
        math_result = math.log(base)

        print(f"ln((x+1)/(x-1)) value at x = {x}:")
        print(f"Approximation result: {result}")
        print(f"Amount of steps used for the approximation: {n}")
        print(f"ln((x+1)/(x-1)) value using math module: {math_result}")

    except ValueError:
        print("Error: Please enter valid numerical inputs.")


def main_1():
    """
    Main function to run the program.
    """
    while True:
        user_interface()
        choice = input("Do you want to calculate again? (yes/no): ").lower()
        if choice != 'yes':
            print("Exiting the program.")
            break