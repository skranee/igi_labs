# Classes needed for building the figure

from abc import ABC, abstractmethod


class GeometricFigure(ABC):

    # Calculates area of the triangle.
    @abstractmethod
    def area(self):
        pass


class Color:

    # Initialization with color.
    def __init__(self, color):
        self._color = color

    # Returns the color of the triangle.
    @property
    def color(self):
        return self._color


class Rectangle(GeometricFigure):
    # Initialize.
    def __init__(self, width, height, color):
        self._width = width
        self._height = height
        self._color = Color(color)

    # Returns area.
    def area(self):
        return self._width * self._height

    # Returns the description.
    def description(self):
        return f"Rectangle with width={self._width}, height={self._height}, color={self._color.color}"
