from rectangle import Rectangle
from circle import Circle
from square import Square
from colorama import Fore, Style

def main():
    N = 5

    rect = Rectangle(N, N, "синий")
    circle = Circle(N, "зеленый")
    square = Square(N, "красный")

    print(Fore.BLUE + rect.__repr__())
    print(Fore.GREEN + circle.__repr__())
    print(Fore.RED + square.__repr__())
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()

