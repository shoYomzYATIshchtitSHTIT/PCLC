from geometric_figure import GeometricFigure
from color_figure import ColorFigure

class Rectangle(GeometricFigure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = ColorFigure(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {} с площадью {}".format(
            self.FIGURE_TYPE, self.color.color, self.width, self.height, self.area()
        )
