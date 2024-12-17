import math
from geometric_figure import GeometricFigure
from color_figure import ColorFigure

class Circle(GeometricFigure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = ColorFigure(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    def __repr__(self):
        return "{} {} цвета радиусом {} с площадью {}".format(
            self.FIGURE_TYPE, self.color.color, self.radius, self.area()
        )
