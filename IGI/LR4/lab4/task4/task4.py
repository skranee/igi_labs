# Lab 4: Triangle building
# Version 1.0
# Developer: Abmetko Pavel
# Date: 04.13.2024

from geometric_figures import GeometricFigure
import matplotlib.pyplot as plt


class IsoscelesTriangle(GeometricFigure):
    def __init__(self, base, height, color):
        self._base = base
        self._height = height
        self._color = color

    def area(self):
        return 0.5 * self._base * self._height

    def draw(self):
        x = [0, self._base / 2, self._base, 0]
        y = [0, self._height, 0, 0]

        plt.fill(x, y, color=self._color)

        plt.title('Triangle')
        plt.xlabel('X')
        plt.ylabel('Y')

        plt.grid(True)
        plt.axis('equal')
        plt.show()


def main():
    while True:
        try:
            base = int(input("Enter the base of the isosceles triangle: "))
            height = int(input("Enter the height of the isosceles triangle: "))
            color = str(input("Enter the color of the triangle: "))

            triangle = IsoscelesTriangle(base, height, color)
            print("Area:", triangle.area())
            triangle.draw()

        except ValueError:
            print("Error: Please enter valid numerical inputs.")

        choice = input("\nDo you want to run the program again? (yes/no): ").lower()
        if choice != "yes":
            print("Exiting the program.")
            break


if __name__ == "__main__":
    main()
