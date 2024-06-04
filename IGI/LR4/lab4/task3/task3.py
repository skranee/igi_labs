import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats


class SequenceAnalyzer:
    def __init__(self, sequence):
        """
        Initializes a SequenceAnalyzer object with a given sequence.

        :param sequence: The input sequence.
        """
        self.sequence = sequence

    def calculate_series(self, x, n):
        """
        Calculates the series expansion of ln((x + 1) / (x - 1)) up to the nth term.

        :param x: The value of x.
        :param n: The number of terms in the series.
        :return: The sum of the series expansion.
        """
        series_sum = 0
        for i in range(1, n + 1):
            series_sum += 2 * (1 / ((2 * i + 1) * math.pow(x, (2 * i + 1))))
        return series_sum

    def analyze_sequence(self):
        """
        Analyzes the input sequence and calculates its mean, median, mode, variance, and standard deviation.

        :return: A dictionary containing the analysis results.
        """
        mean = np.mean(self.sequence)
        median = np.median(self.sequence)
        mode = stats.mode(self.sequence).mode
        if isinstance(mode, np.ndarray):
            mode = mode[0]
        variance = np.var(self.sequence)
        std_deviation = np.std(self.sequence)
        return {
            'mean': mean,
            'median': median,
            'mode': mode,
            'variance': variance,
            'standard_deviation': std_deviation
        }

    def plot_series_comparison(self, x_values, series_values, math_values):
        """
        Plots a comparison between the series expansion and the math function.

        :param x_values: The values of x for the plot.
        :param series_values: The values of the series expansion.
        :param math_values: The values of the math function.
        """
        plt.plot(x_values, series_values, label='Series Expansion')
        plt.plot(x_values, math_values, label='Math Function')
        plt.xlabel('x')
        plt.ylabel('ln(1+x)')
        plt.title('Comparison of Series Expansion and Math Function')
        plt.legend()
        plt.grid(True)

        plt.xlim(-10, 100)
        plt.ylim(-1, 2)

        plt.savefig('plot.png')
        plt.show()

    def find_terms_for_accuracy(self, x, target_accuracy):
        """
        Finds the number of terms needed in the series expansion to achieve the specified accuracy.

        :param x: The value of x.
        :param target_accuracy: The target accuracy.
        :return: The number of terms needed.
        """
        series_sum = 0
        n = 0
        while abs(series_sum - math.log((x + 1) / (x - 1))) > target_accuracy:
            n += 1
            series_sum = self.calculate_series(x, n)
        return n


def input_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if abs(value) < 1:
                print("Can not be |x| < 1")
            else:
                return value
        except ValueError:
            print("Error.")


def display_results(x, approx, n, math_val, eps):
    print("-" * 50)
    print("x\t  n\tF(x)\tMath(F(x))\teps")
    print(f"{x}\t {n}\t{approx:.3f}\t{math_val:.3f}\t        {eps}")
    print("-" * 50)
    print("Result :")
    print(f"F(x) - {approx:.10f}\tMath(F(x)) - {math_val:.10f}\n")


def ln_approximation(x, eps=1e-12, max_iterations=500):
    result = 0
    for n in range(1, max_iterations + 1):
        term = -((math.pow(-2, n)) * math.pow(1 / (-1 + x), n)) / n
        # term = 2 * (1 / ((2 * n + 1) * math.pow(x, (2 * n + 1))))
        result += term
        if abs(term) < eps:
            break
    return result, n


def main():
    x_values = np.linspace(1 + 10e-12, 100, 100000)

    # Create an instance of SequenceAnalyzer class
    sequence_analyzer = SequenceAnalyzer(x_values)

    # Construct a graph comparing a series and a mathematical function
    series_values = [sequence_analyzer.calculate_series(x, 10) for x in x_values]
    math_values = [np.log(((x + 1) / (x - 1))) for x in x_values]
    sequence_analyzer.plot_series_comparison(x_values, series_values, math_values)

    # Analyze the sequence
    analysis_results = sequence_analyzer.analyze_sequence()

    # Output the analysis results to the console
    print("Mean:", analysis_results['mean'])
    print("Median:", analysis_results['median'])
    print("Mode:", analysis_results['mode'])
    print("Variance:", analysis_results['variance'])
    print("Standard Deviation:", analysis_results['standard_deviation'])

    while True:
        x = input_float("Enter x: ")
        eps = float(input("Enter precision (eps): "))

        # Calculating the approximate value of a function
        approx, n = ln_approximation(x, eps)

        # Calculating the value of a function using the module math
        math_val = math.log((x + 1) / (x - 1))

        # Results output
        display_results(x, approx, n, math_val, eps)

        choice = input("Want to calculate again (yes/no)? ").lower()
        if choice != "yes":
            break


if __name__ == "__main__":
    main()
