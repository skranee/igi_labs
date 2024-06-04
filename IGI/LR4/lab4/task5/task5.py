# Lab 4: NumPy Exploring
# Version 1.0
# Developer: Abmetko Pavel
# Date: 04.13.2024

import numpy as np

class NumPyTask:
    """
    Class to perform NumPy tasks as specified in the assignment.
    """

    @staticmethod
    def generate_random_matrix(n, m):
        """
        Generates a random integer matrix of size n x m.

        Parameters:
        - n (int): Number of rows in the matrix.
        - m (int): Number of columns in the matrix.

        Returns:
        - np.ndarray: Random integer matrix.
        """
        return np.random.randint(1, 100, size=(n, m))

    @staticmethod
    def find_column_with_smallest_sum(matrix):
        """
        Finds the column with the smallest sum of elements in the given matrix.

        Parameters:
        - matrix (np.ndarray): Input matrix.

        Returns:
        - int: Index of the column with the smallest sum.
        """
        column_sums = np.sum(matrix, axis=0)
        return np.argmin(column_sums)

    @staticmethod
    def calculate_median_stdlib(matrix, column_index):
        """
        Calculates the median of the specified column using NumPy's median function.

        Parameters:
        - matrix (np.ndarray): Input matrix.
        - column_index (int): Index of the column for which median is to be calculated.

        Returns:
        - float: Median of the specified column.
        """
        column_values = matrix[:, column_index]
        return np.median(column_values)

    @staticmethod
    def calculate_median_formula(matrix, column_index):
        """
        Calculates the median of the specified column using formula.

        Parameters:
        - matrix (np.ndarray): Input matrix.
        - column_index (int): Index of the column for which median is to be calculated.

        Returns:
        - float: Median of the specified column.
        """
        column_values = matrix[:, column_index]
        sorted_values = np.sort(column_values)
        n = len(sorted_values)
        if n % 2 == 0:
            return (sorted_values[n // 2 - 1] + sorted_values[n // 2]) / 2
        else:
            return sorted_values[n // 2]

    @staticmethod
    def main():
        """
        Main function to execute the program.
        """
        try:
            n = int(input("Enter the number of rows in the matrix: "))
            m = int(input("Enter the number of columns in the matrix: "))
            if n <= 0 or m <= 0:
                raise ValueError("Number of rows and columns must be positive integers.")
        except ValueError as e:
            print(f"Error: {e}")
            return

        matrix = NumPyTask.generate_random_matrix(n, m)
        print("Generated Matrix:")
        print(matrix)

        smallest_column_index = NumPyTask.find_column_with_smallest_sum(matrix)
        print(f"\nColumn with the smallest sum of elements: {smallest_column_index}")

        median_stdlib = NumPyTask.calculate_median_stdlib(matrix, smallest_column_index)
        print(f"\nMedian of the specified column (using numpy): {median_stdlib}")

        median_formula = NumPyTask.calculate_median_formula(matrix, smallest_column_index)
        print(f"Median of the specified column (using formula): {median_formula}")


if __name__ == "__main__":
    while True:
        NumPyTask.main()
        choice = input("\nDo you want to run the program again? (yes/no): ").lower()
        if choice != "yes":
            print("Exiting the program.")
            break
