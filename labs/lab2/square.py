from rectangle import Rectangle

class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "{} {} цвета со стороной {} и площадью {}".format(
            self.FIGURE_TYPE, self.color.color, self.width, self.area()
        )
